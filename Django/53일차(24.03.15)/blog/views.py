from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from rest_framework import serializers
from drf_spectacular.utils import extend_schema


# @api_view(["GET"])
# def blog_list(request):
#     blogs = Post.objects.all()
#     serializer = []
#     for blog in blogs:
#         serializer.append(
#             {
#                 "title": blog.title,
#                 "content": blog.content,
#                 "created_at": blog.created_at,
#                 "updated_at": blog.updated_at,
#             }
#         )
#     return Response(serializer)

# @api_view(["POST"])
# def blog_list(request):
#     blogs = Post.objects.all()
#     serializer = []
#     for blog in blogs:
#         serializer.append(
#             {
#                 "title": blog.title,
#                 "content": blog.content,
#                 "created_at": blog.created_at,
#                 "updated_at": blog.updated_at,
#             }
#         )
#     return Response(serializer)

# # GET과 POST 둘 다 접속 가능
# @api_view(['GET', "POST"])
# def blog_list(request):
#     if request.method == 'GET':
#         return Response('hello1')
#     elif request.method == 'POST':
#         return Response('hello2')




# 이 코드는 원래 .serializers.py로 작성이 되었어야 하는 파일입니다.
class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


@extend_schema(
    methods=["GET", "POST"],
    request=PostSerializer,
    responses={200: PostSerializer(many=True)},
)
@api_view(["GET", "POST"])
def blog_list(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)