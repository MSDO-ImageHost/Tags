import pika
import json
from . import sender, receiver

def callback(channel, method, properties, body):
    event = method.routing_key
    body = json.loads(body)
    print(method)
    print(properties)
    print(body)
    print(receiver.receive(event, body))

def send(event: str, body: str):
    pass
    channel.basic_publish(exchange='rapid', routing_key=event, body=body)

def receive():
    for event in events:
        channel.queue_bind(queue='tags', exchange='rapid', routing_key=event)
    
    channel.basic_consume(queue='tags', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='rapid', exchange_type='direct')
channel.queue_declare('tags')

events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'ReqeustTag', 'RequestTagsForPost']
