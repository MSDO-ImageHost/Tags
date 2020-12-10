from . import tag_requests
from .messaging import RabbitMQ
from api.models import Tag, TaggedPost

def test() -> None:
    tags = tag_requests.request_tags_for_post(jwt={}, post_id=1337)
    print(tags)

def main() -> None:
    events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'RequestTag', 'RequestTagsForPost', 'RequestPostsForTag']
    rabbitmq = RabbitMQ()
    rabbitmq.setup(events)
    rabbitmq.receive()
    
def run() -> None:
    test()
