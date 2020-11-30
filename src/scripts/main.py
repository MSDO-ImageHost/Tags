from . import tag_requests
from . import tag_responses
from .messaging import RabbitMQ
from typing import Dict

def test() -> None:
    #create_tag("leet", "This is a description", 1337, 420)
    #print(update_tag(1, "Updated name", "Updated description"))
    tags = tag_requests.request_tags_for_post(post_id=1337)
    print(tag_responses.return_tags_for_post(tags))



def run() -> None:
    tags = tag_requests.request_tags_for_post(post_id=1337)
    #rabbitmq.send("ReturnTagsForPost", return_tags_for_post(tags))
    events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'RequestTag', 'RequestTagsForPost']
    rabbitmq = RabbitMQ()
    rabbitmq.setup()
    rabbitmq.receive(events)
