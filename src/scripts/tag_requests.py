from django.db.models.query import QuerySet
from api.models import Tag

def create_tag(tag_name: str, tag_desc: str, post_id: int, author_id: int) -> Tag:
    tag = Tag(name=tag_name, description=tag_desc, post_id=post_id, author_id=author_id)
    tag.save()
    return tag

def update_tag(tag_id: int, new_name: str, new_desc: str) -> Tag:
    tag = Tag.objects.get(id=tag_id)
    tag.name = new_name
    tag.description = new_desc
    tag.save()
    return tag

def delete_tag(tag_id: int) -> None:
    tag = Tag.objects.get(id=tag_id)
    tag.delete()

def request_tag(tag_id: int) -> Tag:
    return Tag.objects.get(id=tag_id)

def request_tags_for_post(post_id: int) -> QuerySet[Tag]:
    return Tag.objects.filter(post_id=post_id)
