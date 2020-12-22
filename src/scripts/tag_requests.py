import datetime

from typing import Dict, List
from api.models import Tag, TaggedPost

def create_tag(user_id: int, tag_name: str, tag_desc: str = None) -> Dict:
    try:
        tag = Tag.objects.get(name=tag_name, author_id=user_id)
        return f"Tag with name [{tag.name}] and author [{tag.author_id}] already exists"
    except Tag.DoesNotExist:
        tag = Tag(name=tag_name, description=tag_desc, author_id=user_id)
        tag.save()
    return {
        "tag_id": tag.id, 
        "created_at": tag.created_at
    }

def update_tag(user_id: int, role: int, tag_id: int, new_name: str, new_desc: str) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    if user_id != tag.author_id and role < 20:
        return "Permission denied"
    tag.name = new_name
    tag.description = new_desc
    tag.save()
    return {"updated_at": tag.updated_at}

def delete_tag(user_id: int, role: str, tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    if user_id != tag.author_id and role < 20:
        return "Permission denied"
    tag.delete()
    return {"deleted_at": datetime.datetime.now()}

def add_tag_to_post(user_id: int, role: int, post_author: int, tag_id: int, post_id: str) -> Dict:
    if role < 20:
        if user_id != post_author:
            return f"User does not own post with id [{post_id}]"
    tag = Tag.objects.get(id=tag_id)
    try:
        TaggedPost.objects.get(tag__id=tag_id, post_id=post_id)
        return f"Post [{post_id}] is already tagged with tag with id [{tag_id}]"
    except TaggedPost.DoesNotExist:
        tagged_post = TaggedPost(tag=tag, post_id=post_id, tagger_id=user_id)
        tagged_post.save()
        return {
            "tag_id": tag.id,
            "post_id": post_id
        }

def add_tags_to_post(user_id: int, role: int, post_author: int, tag_names: List[str], post_id: str) -> List:
    if role < 20:
        if user_id != post_author:
            return f"User does not own post with id [{post_id}]"

    responses = []
    for tag_name in tag_names:
        try:
            tag = Tag.objects.get(name=tag_name, author_id=user_id)
        except Tag.DoesNotExist:
            tag = Tag(name=tag_name, author_id=user_id)
            tag.save()
        responses.append(add_tag_to_post(user_id, role, post_author, tag.id, post_id))
    return responses


def remove_tag_from_post(user_id: int, role: int, post_author: int, tag_id: int, post_id: str) -> Dict:
    if role < 20:
        if user_id != post_author:
            return f"User does not own post with id [{post_id}]"
    tagged_post = TaggedPost.objects.get(tag__id=tag_id, post_id=post_id)
    tagged_post.delete()
    return {"removed_at": datetime.datetime.now()}

def request_tag(tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    return tag.serialize()

def request_tags_for_post(post_id: int) -> List:
    tagged_posts = TaggedPost.objects.filter(post_id=post_id)
    return [tp.tag.serialize() for tp in tagged_posts]

def request_posts_for_tag(tag_id: int) -> List:
    tagged_posts = TaggedPost.objects.filter(tag__id=tag_id)
    return [{"post_id": tp.post_id} for tp in tagged_posts]
