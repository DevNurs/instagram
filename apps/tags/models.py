from django.db import models
from apps.posts.models import Post


class Tag(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Тег',
        blank=True, null=True
    )
    post = models.ManyToManyField(
        Post,
        related_name='tags',
    )

    def __str__(self):
        return f"{self.title} -- {self.post.id}"
