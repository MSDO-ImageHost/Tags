from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)
    author_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, description={self.description}, author={self.author_id})"

    def __str__(self):
        return f"id of tag: {self.id}\nName of tag: {self.name}\nTag description: {self.description}\nAuthor id: {self.author_id}\nCreated at: {self.created_at}\nUpdated at: {self.updated_at}"

    def serialize(self):
        return {
            "tag_id": self.id,
            "author": self.author_id,
            "tag_name": self.name,
            "tag_desc": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class TaggedPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=50)
    tagger_id = models.PositiveIntegerField()

    def __repr__(self):
        return f"{type(self).__name__}(tag_id={self.tag.id}, post_id={self.post_id}, post={self.post_id}, tagger_id={self.tagger_id})"

    def __str__(self):
        return f"id of tag: {self.tag.id}\nid of post: {self.post_id}\nid of tagger: {self.tagger_id}"
