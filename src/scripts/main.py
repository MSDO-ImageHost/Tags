from .tag_requests import *
from .tag_responses import *
from . import rabbitmq

def test() -> None:
    #create_tag("leet", "This is a description", 1337, 420)
    #print(update_tag(1, "Updated name", "Updated description"))
    tags = request_tags_for_post(post_id=1337)
    print(return_tags_for_post(tags))

def run() -> None:
    tags = request_tags_for_post(post_id=1337)
    #rabbitmq.send("ReturnTagsForPost", return_tags_for_post(tags))
    rabbitmq.receive()
    #event, body = rabbitmq.receive()
    #print(receive(event, body))
    