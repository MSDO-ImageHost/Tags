import datetime

from typing import Dict, List
from api.models import Tag, TaggedPost

def create_tag(author_id: int, tag_name: str, tag_desc: str) -> Dict:
    tag = Tag(name=tag_name, description=tag_desc, author_id=author_id)
    tag.save()
    return {
        "tag_id": tag.id, 
        "created_at": tag.created_at
    }

def update_tag(user_id: int, role: str, tag_id: int, new_name: str, new_desc: str) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    if user_id != tag.author_id and role != "admin":  # change role to int
        return "Permission denied"
    tag.name = new_name
    tag.description = new_desc
    tag.save()
    return {"updated_at": tag.updated_at}

def delete_tag(user_id: int, role: str, tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    if user_id != tag.author_id and role != "admin":  # change role to int
        return "Permission denied"
    tag.delete()
    return {"deleted_at": datetime.datetime.now()}

def add_tag_to_post(user_id: int, role: str, post_author: int, tag_id: int, post_id: str) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    if role != "admin":   # change role to int
        if user_id != post_author:
            return "User does not own post"
    tagged_post = TaggedPost(tag=tag, post_id=post_id, tagger_id=user_id)
    tagged_post.save()
    return {
        "tag_id": tag.id,
        "post_id": post_id
    }

def remove_tag_from_post(user_id: int, role: str, post_author: int, tag_id: int, post_id: str) -> Dict:
    if role != "admin":   # change role to int
        if user_id != post_author:
            return "User does not own post"
    tagged_post = TaggedPost.objects.get(tag__id=tag_id, post_id=post_id)
    tagged_post.delete()
    return {"removed_at": datetime.datetime.now()}

def request_tag(tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    return tag.serialize()

def request_tags_for_post(post_id: int) -> List:
    tagged_posts = TaggedPost.objects.filter(post_id=post_id)
    return [tp.tag.serialize() for tp in tagged_posts]

def request_posts_for_tags(tag_id: int) -> List:
    tagged_posts = TaggedPost.objects.filter(tag__id=tag_id)
    return [{"post_id": tp.post_id} for tp in tagged_posts]
