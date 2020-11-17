from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Tag(name={self.name}, description={self.description}, author={self.author})"
