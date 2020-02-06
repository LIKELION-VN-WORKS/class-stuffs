from django.utils import timezone
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    # <- Cover title(Charfield) in admin. 관리자 페이지에서 보기 쉽게 이름을 지정해준다.
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content
