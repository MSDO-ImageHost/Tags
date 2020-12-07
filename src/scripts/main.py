from . import tag_requests
from .messaging import RabbitMQ

def test() -> None:
    tags = tag_requests.request_tags_for_post(post_id=1337)
    print(tags)



def run() -> None:
    events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'RequestTag', 'RequestTagsForPost']
    rabbitmq = RabbitMQ()
    rabbitmq.setup(events)
    rabbitmq.receive()
