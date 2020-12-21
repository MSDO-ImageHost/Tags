import pika
import json

from typing import List, Dict, Tuple
from .tag_requests import *
from Tags.settings import AMQP_PASS, AMQP_USER, AMQP_HOST
from .jwt import verify
from jose.exceptions import ExpiredSignatureError, JWTError
from pika.spec import BasicProperties
from django.db.utils import OperationalError


class RabbitMQ:
    
    def __init__(self) -> None:
        credentials = pika.PlainCredentials(AMQP_USER, AMQP_PASS)
        print("Establishing connection...")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=AMQP_HOST,
            port=5672,
            virtual_host='/',
            credentials=credentials))
        print("Connection established!")
        self.channel = self.connection.channel()

    def setup(self, events: List[str]) -> None:
        self.channel.exchange_declare(exchange='rapid', exchange_type='direct')
        self.channel.queue_declare(queue='tags')
        for event in events:
            self.channel.queue_bind(queue='tags', exchange='rapid', routing_key=event)
        print("Setup done")

    def send(self, event: str, body: str, properties: Dict) -> None:
        self.channel.basic_publish(exchange='rapid', routing_key=event, body=body, properties=properties)
        self.connection.close()
        
    def receive(self) -> None:
        self.channel.basic_consume(queue='tags', on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()


def callback(channel, method, properties, body) -> None:
    event = method.routing_key
    body = json.loads(body)
    receive(event, body, properties)

def send(event: str, data: Dict, status_code: int, message: str, correlation_id: str, content_type: str):
    rabbitmq = RabbitMQ()
    body = json.dumps(data, indent=4, default=str)
    headers = {"status_code": status_code, "message": message}
    properties = BasicProperties(content_type=content_type, headers=headers, correlation_id=correlation_id)
    print("Sending event:", event)
    print("Body:", data)
    print(headers)
    rabbitmq.send(event, body, properties)
    print("Done sending")
    restart = status_code == 503
    print("Restarting after sending:", restart)
    if restart:
        raise Exception("Restarting due to database connection error")

def handle_event(event: str, body: Dict, jwt: Dict, auth_needed: bool) -> Tuple:
    if auth_needed:
        user_id = int(jwt["sub"])
        role = int(jwt["role"])

        if event == "CreateTag":
            return (
                create_tag(user_id, body["tag_name"], body["tag_desc"]),
                200,
                "OK"
            )

        elif event == "UpdateTag":
            tag_id = body["tag_id"]
            try:
                update = update_tag(user_id, role, tag_id, body["new_name"], body["new_desc"])
            except Tag.DoesNotExist:
                return ({}, 404, "Tag not found")
            if isinstance(update, str):
                return ({}, 403, update)
            return (update, 200, "OK")
                
        elif event == "DeleteTag":
            tag_id = body["tag_id"]
            try:
                delete = delete_tag(user_id, role, tag_id)
            except Tag.DoesNotExist:
                return ({}, 404, "Tag not found")
            if isinstance(delete, str):
                return ({}, 403, delete)
            return (delete, 200, "OK")

        elif event == "AddTagToPost":
            tag_id = body["tag_id"]
            post_id = body["post_id"]
            post_author = body["post_author"]
            try:
                tagged_post = add_tag_to_post(user_id, role, post_author, tag_id, post_id)
            except Tag.DoesNotExist:
                return ({}, 404, "Tag not found")
            if isinstance(tagged_post, str):
                return ({}, 403, tagged_post)
            return (tagged_post, 200, "OK")

        elif event == "RemoveTagFromPost":
            tag_id = body["tag_id"]
            post_id = body["post_id"]
            post_author = body["post_author"]
            try:
                removed_tag = remove_tag_from_post(user_id, role, post_author, tag_id, post_id)
            except TaggedPost.DoesNotExist:
                return ({}, 404, "Post does not have that tag")
            if isinstance(removed_tag, str):
                if removed_tag == "User does not own post":
                    error_code = 403
                else:
                    error_code = 400
                return ({}, error_code, removed_tag)
            return (removed_tag, 200, "OK")

    else:
        
        if event == "RequestTag":
            tag_id = body["tag_id"]
            try:
                data = request_tag(tag_id)
                return (data, 200, "OK")
            except Tag.DoesNotExist:
                return ({}, 404, "Tag not found")
        
        elif event == "RequestTagsForPost":
            return (request_tags_for_post(body["post_id"]), 200, "OK")
        
        elif event == "RequestPostsForTag":
            return (request_posts_for_tags(body["tag_id"]), 200, "OK")
    

def check_jwt(jwt_token: str):
    try:
        verify(jwt_token)
    except (ExpiredSignatureError, JWTError) as e:
        print(e)
        return False
    return True

def receive(event: str, body: Dict, properties: BasicProperties):
    responses = {
        "CreateTag": "ConfirmTagCreation",
        "UpdateTag": "ConfirmTagUpdate",
        "DeleteTag": "ConfirmTagDeletion",
        "AddTagToPost": "ConfirmAddedTag",
        "RemoveTagFromPost": "ConfirmTagRemoval",
        "RequestTag": "ReturnTag",
        "RequestTagsForPost": "ReturnTagsForPost",
        "RequestPostsForTag": "ReturnPostsForTag"
    }

    response_event = responses[event]
    body = {key.lower(): value for key, value in body.items()}
    jwt_token = properties.headers["jwt"]
    correlation_id = properties.correlation_id
    content_type = properties.content_type
    decoded_token = {}
    auth_needed = False
    
    if event in ["CreateTag", "UpdateTag", "DeleteTag", "AddTagToPost", "RemoveTagFromPost"]:
        if check_jwt(jwt_token):
            decoded_token = verify(jwt_token)
            auth_needed = True
        else:
            send(
                event=response_event,
                data={},
                status_code=401,
                message="Invalid token",
                correlation_id=correlation_id,
                content_type=content_type
            )
    try:
        response_data, code, message = handle_event(event, body, decoded_token, auth_needed)
    except OperationalError:
        response_data = {}
        code = 503
        message = "Lost database connection"
    send(
        event=response_event,
        data=response_data,
        status_code=code,
        message=message,
        correlation_id=correlation_id,
        content_type=content_type
    )
