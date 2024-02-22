from django.urls import path
from . import views # from . 은 현재폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]