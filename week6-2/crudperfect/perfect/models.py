from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=200)
    contents = models.TextField()
    price = models.IntegerField()
    RATING = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),)
    rating = models.CharField(max_length=1, choices=RATING, default='1',)
    img = models.FileField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
