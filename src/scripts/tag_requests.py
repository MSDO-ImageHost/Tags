import datetime

from typing import Dict, List
from api.models import Tag, TaggedPost

def create_tag(jwt: Dict, tag_name: str, tag_desc: str) -> Dict:
    author_id = jwt['sub']
    tag = Tag(name=tag_name, description=tag_desc, author_id=author_id)
    tag.save()
    return {
        "tag_id": tag.id, 
        "created_at": tag.created_at
    }

def update_tag(jwt: Dict, tag_id: int, new_name: str, new_desc: str) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    tag.name = new_name
    tag.description = new_desc
    tag.save()
    return {
        "updated_at": tag.updated_at
    }

def delete_tag(jwt: Dict, tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return {
        "deleted_at": datetime.datetime.now()
    }

def add_tag_to_post(jwt: Dict, tag_id: int, post_id: str) -> Dict:
    tagger_id = jwt['sub']
    tag = Tag.objects.get(id=tag_id)
    tagged_post = TaggedPost(tag=tag, post_id=post_id, tagger_id=tagger_id)
    tagged_post.save()
    return {
        "tag_id": tag_id,
        "post_id": post_id
    }

def request_tag(jwt: Dict, tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    return tag.serialize()

def request_tags_for_post(jwt: Dict, post_id: int) -> List:
    tagged_posts = TaggedPost.objects.filter(post_id=post_id)
    return [tp.tag.serialize() for tp in tagged_posts]

def request_posts_for_tags(jwt: Dict, tag_id: int) -> List:
    tagged_posts = TaggedPost.objects.filter(tag__id=tag_id)
    return [{"post_id": tp.post_id} for tp in tagged_posts]
