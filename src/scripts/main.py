from . import tag_requests
from .messaging import RabbitMQ
from api.models import Tag, TaggedPost

def test() -> None:
    tags = Tag.objects.all()
    tagged_posts = TaggedPost.objects.all()
    for tp in tagged_posts:
        print(tp)
        print()
    print()
    for tag in tags:
        print(tag)
        print()

def main() -> None:
    events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'AddTagToPost', 'RequestTag', 'RequestTagsForPost', 'RequestPostsForTag']
    rabbitmq = RabbitMQ()
    rabbitmq.setup(events)
    rabbitmq.receive()
    
def run() -> None:
    main()
