from django.contrib import admin
from .models import Post, Comment, Tag

admin.site.register(Post) # Post DB 내용과
admin.site.register(Comment) # Comment DB 내용과
admin.site.register(Tag) # Tag DB 내용을 admin 페이지에 반영