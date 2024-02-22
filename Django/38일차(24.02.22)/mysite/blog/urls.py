from django.urls import path
from . import views # from . 은 현재폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]

