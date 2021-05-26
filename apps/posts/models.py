from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='posts',
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='post',
        verbose_name='Картины'
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание'
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.id}"
