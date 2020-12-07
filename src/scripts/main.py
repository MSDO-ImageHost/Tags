from . import tag_requests
from .messaging import RabbitMQ

def test() -> None:
    #create_tag("leet", "This is a description", 1337, 420)
    #print(update_tag(1, "Updated name", "Updated description"))
    tags = tag_requests.request_tags_for_post(post_id=1337)
    print(tags)



def run() -> None:
    events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'RequestTag', 'RequestTagsForPost']
    rabbitmq = RabbitMQ()
    rabbitmq.setup(events)
    rabbitmq.receive()
