import json
import datetime

from django.db.models.query import QuerySet
from api.models import Tag
from typing import List

def confirm_tag_creation(tag: Tag) -> str:
    return json.dumps({
        "tag_id": tag.id, 
        "status_code": 200, 
        "created_at": tag.created_at
    }, indent=4, default=str)

def confirm_tag_update(tag: Tag) -> str:
    return json.dumps({
        "status_code" : 200,
        "updated_at": tag.updated_at
    }, indent=4, default=str)

def confirm_tag_deletion() -> str:
    return json.dumps({
        "status_code": 200,
        "deleted_at": datetime.datetime.now()
    }, indent=4, default=str)

def return_tag(tag: Tag) -> str:
    return json.dumps({
        "post": tag.post_id,
        "author": tag.author_id,
        "tag_name": tag.name,
        "tag_desc": tag.description,
        "created_at": tag.created_at,
        "updated_at": tag.updated_at
    }, indent=4, default=str)

def return_tags_for_post(tags: QuerySet[Tag]) -> str:
    serialized = [{
        "post": tag.post_id,
        "author": tag.author_id,
        "tag_name": tag.name,
        "tag_desc": tag.description,
        "created_at": tag.created_at,
        "updated_at": tag.updated_at
    } for tag in tags]
    return json.dumps(serialized, indent=4, default=str)
