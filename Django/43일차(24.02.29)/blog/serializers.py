from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta: # Post의 모든 필드를 직렬화/역직렬화를 자동으로 해준다.
        model = Post
        fields = '__all__'