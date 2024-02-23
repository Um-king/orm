# admin page에서 BLOG > POST 에서 게시물을 추가했을때 해당 내용을 가져온다.
# 가져온 사이트 POST 데이터들을 Post class에 할당한다.

from django.contrib import admin
from .models import Post # models.py의 클래스명

# models.py의 클래스명 = Post
# admin site의 POST 게시물을 Post class 객체에 할당
# admin site의 POST 데이터들과 Post class 와 연결
admin.site.register(Post) # admin page 커스터마이징은 뒤에서 배웁니다.