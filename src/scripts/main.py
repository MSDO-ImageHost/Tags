from . import tag_requests
from .messaging import RabbitMQ
from api.models import Tag, TaggedPost

def test() -> None:
    user_id = 42
    role = 0
    post_author = 42
    tag_names = ["food", "art", "stuff"]
    post_id = "niceid"
    #print(tag_requests.add_tags_to_post(user_id, role, post_author, tag_names, post_id))

def main() -> None:
    events = ['CreateTag', 'UpdateTag', 'DeleteTag', 'AddTagToPost', 'RemoveTagFromPost', 'RequestTag', 'RequestTagsForPost', 'RequestPostsForTag', 'ConfirmOnePostCreation']
    rabbitmq = RabbitMQ()
    rabbitmq.setup(events)
    rabbitmq.receive()
    
def run() -> None:
    main()
