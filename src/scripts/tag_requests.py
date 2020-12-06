import datetime
from typing import Dict

from django.db.models.query import QuerySet
from api.models import Tag

def create_tag(jwt: Dict, tag_name: str, tag_desc: str, post_id: int) -> Dict:
    author_id = jwt['sub']
    tag = Tag(name=tag_name, description=tag_desc, post_id=post_id, author_id=author_id)
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

def request_tag(jwt: Dict, tag_id: int) -> Dict:
    tag = Tag.objects.get(id=tag_id)
    return {
        "post": tag.post_id,
        "author": tag.author_id,
        "tag_name": tag.name,
        "tag_desc": tag.description,
        "created_at": tag.created_at,
        "updated_at": tag.updated_at
    }

def request_tags_for_post(jwt: Dict, post_id: int) -> Dict:
    tags = Tag.objects.filter(post_id=post_id)
    return [{
        "tag_id": tag.id,
        "post": tag.post_id,
        "author": tag.author_id,
        "tag_name": tag.name,
        "tag_desc": tag.description,
        "created_at": tag.created_at,
        "updated_at": tag.updated_at
    } for tag in tags]
