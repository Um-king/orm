from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    main_image = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성될 때만 추가
    updated_at = models.DateTimeField(auto_now=True)  # 수정할 때마다 추가

    def __str__(self):
        return self.title