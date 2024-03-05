from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/")
    video_file = models.FileField(upload_to="blog/files/%Y/%m/%d/")
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True) # 다대다 관계 -> post에서 tag로 tag에서 post로 연결 가능
    # ManyToManyField : n:n -> 다대다 관계를 설정

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # User가 1, (ForeignKey 뒤에 있는 거는 1), Comment가 n(그위에 있는 것은 n)
    # 외래키 설정
    
    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
# 구독자와 채널 소유자 user간의 중계 테이블 생성(user와 user 연결하는 중간 테이블)
class Subscription(models.Model): # 중계테이블 생성(user와 user를 연결하는 중간테이블)
    subscriber = models.ForeignKey( # 구독자 user 정보
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    channel = models.ForeignKey( # 채널 소유자 user 정보
        User, on_delete=models.CASCADE, related_name="subscribers"
    ) 
    subscribed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("subscriber", "channel")  # 구독자와 채널은 유일해야 함

    def __str__(self):
        return f"{self.subscriber.username}이 {self.channel.username}를 구독하였습니다."