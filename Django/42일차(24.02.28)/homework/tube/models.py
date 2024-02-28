from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    video_file = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # User:Post = 1:N / User : django에서 기본 제공하는 모듈
    tags = models.ManyToManyField("Tag", blank=True) # Tag 필드 참조(Tag 필드는 Tag class로 생성)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") # 출력 페이지에서 comments 이름으로 호출 가능하다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name