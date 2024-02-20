from django.contrib import admin
from django.urls import path
from main.views import (
    index, 
    about, 
    notice, 
    notice1, 
    notice2, 
    notice3, 
    contact, 
    d, 
    hojun,
    mini
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('notice/', notice),
    path('notice/1/', notice1),
    path('notice/2/', notice2),
    path('notice/3/', notice3),
    path('contact/', contact),
    path('a/b/c/d/', d),
    path('user/hojun/', hojun),
    path('user/mini/', mini),

]

# 이렇게 작성하면 100개가 된다면 100개를 작성해야함.. 따라서 동적으로 생성해줘야함
# path('notice/1/', notice1),
# path('notice/2/', notice2),
# path('notice/3/', notice3),

# 이런식으로 작성함 => url 경로 입력 시 notice/1 이렇게 입력하면 1 의 값이 pk값으로 사용되고 경로의 notice가 함수로 활용됨
# path('notice/<int:pk>/', notice)  
# path('user/<str:s>/', user)