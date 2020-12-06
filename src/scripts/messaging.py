from jose.jwt import decode
import pika
import json

from typing import List, Dict, Optional
from .tag_requests import *
from .tag_responses import *
from api.models import Tag
from Tags.settings import AMQP_PASS, AMQP_URI, AMQP_USER
from .jwt import verify
from jose.exceptions import ExpiredSignatureError, JWTError
from pika.spec import BasicProperties

from scripts import jwt


class RabbitMQ:
    
    def __init__(self) -> None:
        credentials = pika.PlainCredentials(AMQP_USER, AMQP_PASS)
        print("Establishing connection...")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='rabbitmq',
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
        print("Sent event:", event)

    def receive(self) -> None:
        self.channel.basic_consume(queue='tags', on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()


def callback(channel, method, properties, body) -> None:
    event = method.routing_key
    body = json.loads(body)
    jwt_token = properties.headers['jwt']
    correlation_id = properties.correlation_id
    content_type = properties.content_type
    body, properties = receive(event, body, jwt_token, correlation_id, content_type)
    print(body)
    print(properties.correlation_id)
    print(properties.content_type)
    print(properties.headers)

def send(event: str, data: Dict, jwt: str, status_code: int, message: str, correlation_id: str, content_type: str) -> str:
    rabbitmq = RabbitMQ()
    body = json.dumps(data, indent=4, default=str)
    headers = {"jwt": jwt, "status_code": status_code, "message": message}
    properties = BasicProperties(content_type=content_type, headers=headers, correlation_id=correlation_id)
    rabbitmq.send(event, body, properties)
    return (body, properties)

def receive(event: str, body: Dict, jwt_token: str, correlation_id, content_type: str) -> str:
    responses = {
        "CreateTag": (create_tag, "ConfirmTagCreation"),
        "UpdateTag": (update_tag, "ConfirmTagUpdate"),
        "DeleteTag": (delete_tag, "ConfirmTagDeletion"),
        "RequestTag": (request_tag, "ReturnTag"),
        "RequestTagsForPost": (request_tags_for_post, "ReturnTagsForPost")
    }

    decoded_token = {}
    body = {key.lower(): value for key, value in body.items()}
    response_event = responses[event][1]

    try:
        decoded_token = verify(jwt_token)
    except (ExpiredSignatureError, JWTError):
        return send(
            event=response_event,
            data={},
            jwt=jwt_token,
            status_code=401,
            message="Invalid token",
            correlation_id=correlation_id,
            content_type=content_type
        )

    try:
        response_data = responses[event][0](decoded_token, **body)
    except Tag.DoesNotExist:
        return send(
            event=response_event,
            data={},
            jwt=jwt_token,
            status_code=404,
            message="Tag not found",
            correlation_id=correlation_id,
            content_type=content_type
        )
    return send(
        event=response_event,
        data=response_data,
        jwt=jwt_token,
        status_code=200,
        message="OK",
        correlation_id=correlation_id,
        content_type=content_type
    )
