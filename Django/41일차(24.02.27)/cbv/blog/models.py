from django.db import models

# 실제 DB 필드를 만드는 작업
# 아래 변수들이 실제 DB 필드로 생성된다.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True) # 이미지 업로드
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True) # 동영상 업로드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title