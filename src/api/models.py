from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    post_id = models.PositiveBigIntegerField()
    author_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{type(self).__name__}({self.name}, description={self.description}, post={self.post_id}, author={self.author_id})"

    def __str__(self):
        return f"id of tag: {self.id}\nName of tag: {self.name}\nTag description: {self.description}\nPost id: {self.post_id}\nAuthor id: {self.author_id}\nCreated at: {self.created_at}\nUpdated at: {self.updated_at}"
