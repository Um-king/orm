# notice/urls.py

from django.urls import path
from .views import free, freedetails, onenone, onenonedetails, details

urlpatterns = [
    # # 자유게시판 목록
    # path('free/', free),
    # # 자유게시판 상세 게시물
    # path('free/<int:pk>/', freedetails),
    # # 1:1 상담 안내
    # path('onenone/', onenone),
    # # 1:1 상담 상세 게시물
    # path('onenone/<int:pk>/', onenonedetails),
     # 다중 작성 가능
    path('<str:word>/<int:pk>/', details),
]
