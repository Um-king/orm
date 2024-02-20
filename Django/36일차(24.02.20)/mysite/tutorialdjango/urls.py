from django.contrib import admin
from django.urls import path

# 추가 / main의 앱들을 호출
from main.views import index, a, b, c, hojun, orm

# path의 첫번째 인자는 접속한 url 경로, 두번째 인자는 해당 url로 접속시 어느 화면을 출력할지에 대한 함수명 -> 해당 함수는 main의 views에 정의 되어있고
# main의 views 함수정의내에서 어느 화면을 출력해줄 것인가 정의
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('a/', a), # a/ 처럼 뒤에 /를 반드시 넣어줘야한다.
    path('b/', b),
    path('c/', c),
    path('hojun/', hojun),
    path('orm/', orm), # 앞은 접속 경로, 보여줄 문서를 호출하는 함수
]
