from django.urls import path, include
from .views import index, about, contact

# main과 같은 startapp한 앱들은 urls.py가 자동으로 생성되지 않아서 만들어줘야한다.
# tutorialdjango > urls.py 에서 해당 경로로 접속한 것들은 include로 main > urls.py에서 처리되도록 연결했음
# tutorialdjango > urls.py 에서 전달된 경로에 맞는 path를 찾음
urlpatterns = [
    path("", index), 
    path("about/", about), # 로컬주소/about 의 경로도 여기서 처리. 
    path("contact/", contact),

]