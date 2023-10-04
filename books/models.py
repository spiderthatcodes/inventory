from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True)
    status = models.CharField(
        max_length=50,
        choices=(
            ('read', 'read'),
            ('wishlist', 'wishlist')
        )
    )
    published_on = models.DateField(null=True)
    cover_image = models.URLField(null=True)
    rating = models.FloatField(null=True)
    genre = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='books',
        on_delete=models.CASCADE
    )
