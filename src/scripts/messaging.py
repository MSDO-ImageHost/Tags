import pika
import json

from typing import List, Dict
from . import tag_requests
from . import tag_responses
from api.models import Tag
from Tags.settings import AMQP_PASS, AMQP_USER


class RabbitMQ:
    
    def __init__(self) -> None:
        credentials = pika.PlainCredentials(AMQP_USER, AMQP_PASS)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='rabbitmq',
            port=5672,
            virtual_host='/',
            credentials=credentials
        ))
        #connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()

    def setup(self) -> None:
        self.channel.exchange_declare(exchange='rapid', exchange_type='direct')
        self.channel.queue_declare(queue='tags')

    def send(self, event: str, body: str) -> None:
        self.channel.basic_publish(exchange='rapid', routing_key=event, body=body)

    def receive(self, events: List[str]) -> None:
        for event in events:
            self.channel.queue_bind(queue='tags', exchange='rapid', routing_key=event)
        
        self.channel.basic_consume(queue='tags', on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()


def callback(channel, method, properties, body):
    event = method.routing_key
    body = json.loads(body)
    print(receive(event, body))

def send(event: str, body: str) -> None:
    rabbitmq = RabbitMQ()
    rabbitmq.send(event, body)
    return body

def receive(event: str, body: Dict) -> str:
    body = {key.lower(): value for key, value in body.items()}

    response_event = ""
    response_body = ""

    if event == "CreateTag":
        tag = tag_requests.create_tag(**body)
        response_event = "ConfirmTagCreation"
        response_body = tag_responses.confirm_tag_creation(tag)

    elif event == "UpdateTag":
        response_event = "ConfirmTagUpdate"
        try:
            tag = tag_requests.update_tag(**body)
            response_body = tag_responses.confirm_tag_update(tag)

        except Tag.DoesNotExist:
            response_body = tag_responses.error_response(f"Tag with id {body['tag_id']} was not found.")

    elif event == "DeleteTag":
        response_event = "ConfirmTagDeletion"
        try:
            tag_requests.delete_tag(**body)
            response_body = tag_responses.confirm_tag_deletion()
        except Tag.DoesNotExist:
            response_body = tag_responses.error_response(f"Tag with id {body['tag_id']} was not found.")

    elif event == "RequestTag":
        response_event = "ReturnTag"
        try:
            tag = tag_requests.request_tag(**body)
            response_body = tag_responses.return_tag(tag)
        except Tag.DoesNotExist:
            response_body = tag_responses.error_response(f"Tag with id {body['tag_id']} was not found.")

    elif event == "RequestTagsForPost":
        tags = tag_requests.request_tags_for_post(**body)
        response_event = "ReturnTagsForPost"
        response_body = tag_responses.return_tags_for_post(tags)
    
    return send(response_event, response_body)

