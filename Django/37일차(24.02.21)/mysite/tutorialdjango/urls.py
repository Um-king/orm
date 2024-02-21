from django.contrib import admin
from django.urls import path
from main.views import index, bloglist, blogdetails, userdetails, bookinfo
# from main.views import * 는 최대한 사용하지 말것(함수명이 겹칠때 문제해결을 할 수 없다.)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("blog/", bloglist),
    path("blog/<int:pk>/", blogdetails),
    path("user/<str:user>/", userdetails),
    path("bookinfo/", bookinfo),
]