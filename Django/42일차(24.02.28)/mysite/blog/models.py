from django.db import models
from django.contrib.auth.models import User

# models.py에서 DB를 정의하는 것!
# 여기서 DB 필드나 DB 내용을 정의하면 django가 알아서 DB를 셋팅

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE #db cascade 제약조건 추가!
    ) # cascade : 부모의 정보가 수정/삭제되면 자식의 정보도 같이 수정/삭제 된다.
    
    # 장고에서는 1 : N의 관계를 정의하기 위해 ForeignKey를 사용합니다. 또한 ForeignKey 필드는 1에 정의하는 것이 아니라  N에 정의합니다.
    # '1:N'인 경우 ForeignKey는 N쪽에 작성한다.

    def __str__(self):
        return self.title
