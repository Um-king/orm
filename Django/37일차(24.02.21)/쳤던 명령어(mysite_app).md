# 앱 분기에 대한 실습

```python
# 폴더 기준으로 VSC 열기
#     * 이 작업은 리눅스 명령어 나중에 배울때 까지 똑같은 방식으로 진행하겠습니다.(내가 리눅스 명령어를 좀 안다! 하시는 분은 동일하게 안하셔도 됩니다.)
#     * File > Open Folder 누르시고 Django 작업할 폴더를 열어주세요.

# 터미널을 열어 작업
#     * 터미널(Ctrl + `), 단축키 대신 VSC에서 Terminal > new Terminal
# 이 명령어는 powershell 에서 치고 있습니다.
# 터미널 오른쪽 상단 +버튼 옆 아래 꺾쇠 버튼 눌러스 powershell을 열어주세요.

python --version
# 파이썬 버전 확인
mkdir mysite_app
# mysite라는 폴더 생성 => 마우스 클릭하셔서 생성하는 것과 차이 없습니다. 보통 mysite라는 이름 대신 프로젝트 이름을 넣습니다.
cd mysite
# 폴더 이동
python -m venv venv
# 가상 환경 설정(이어 설명합니다.) 하는 명령어 입니다.

# 가상환경 설정
#     * 가상환경은 선택이 아니라 필수 입니다.
#     * 가상환경을 왜 잡을까요? 관리, 이관, 업데이트 등에 중요한 거점이 됩니다.
#     * pip list를 쳐보세요. 많은 python 라이브러리가 보이죠? 여기서 소숫점 3번째 짜리까지 안맞으면 작동 안되는 경우도 허다합니다. => 가상 환경은 통째로 다 이동합니다.
#     * `python -m venv venv`뒤가 가상환경 이름입니다.

# 가상환경속으로 들어가기
.\venv\Scripts\activate # window
.\venv\Script\activate.bat # window
source ./venv/bin/activate # mac, linux

# window에서 오류가 뜰 경우
+ CategoryInfo          : 보안 오류: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
# 아래 명령어를 입력해주세요. 
# 혹시 이 명령어가 제대로 작동하지 않으면 관리자 권한으로 powershell을 여시고 아래 명령어를 입력해주세요. (혹시 입력해야 하는 창이 있으면 '모두 예'인 'A'를 입력해주세요.)
# VSC를 관리자권한으로 여셔서 작업하셔도 동일한 효과가 납니다.
Set-ExecutionPolicy Unrestricted

# 앞에 (venv) ~~~ 이런 상태에서만 작업을 하셔야 합니다. 이 곳이 가상환경입니다. 쉽게 말해 컴퓨터 안에 컴퓨터입니다!
# pip list 쳐보면 설치된 것이 없는 깨끗한 백지상태입니다.

pip install django
# django를 최신 버전으로 설치합니다. 구버전 설치 하고 싶으시면 pip install django==4.0

django-admin startproject tutorialdjango .
# 띄고 점 꼭 하셔야 합니다!!!! 설치된 django로 초기세팅 하겠다라는 명령어 입니다. 암기하는 명령어 입니다. tutorialdjango는 이름입니다. 여러분 마음대로 지셔도 되는 이름입니다.

python manage.py migrate
# 이 명령어는 우리가 짠 python 코드를 DB에 반영하는 코드입니다. 다만! 실무에서는 이 migrate라는 명령어를 초기 세팅이 다~~~ 끝나고 합니다. 특히 User나 Admin 가입 소스코드를 만지면 먼저 migrate를 하면 error가 나는 경우가 있습니다. 처음에 migrate를 하면 기본적으로 django에서 세팅해주는 소스코드를 DB에 생성, 반영합니다.

python manage.py runserver
# 파이썬 서버를 구동합니다. 이 명령어가 실행되는 동안에만 서버가 실행됩니다. Ctrl 누르고 서버 URL을 클릭해보세요.


################################
# tutorialdjango > settings.py

ALLOWED_HOSTS = ["*"] # 우리 웹 서비스에 접속할 수 있는 사람을 모든사람으로 설정

################################

# URL에 따라 보통 1개의 앱을 만듭니다. 이름만 앱입니다. 실제로 다른 애플리케이션이라는 얘기가 아닙니다. 이유는 권한, 그 안에 들어가는 로직 등을 별도로 관리하기 위해서 입니다. 예를 들어 회원 게시판이 있고 자유 게시판이 있다면 회원 게시판에는 회원만 글을 써야 합니다. 이런 식으로 URL에 따른 권한과 로직을 별도로 관리하기 위해서 앱을 만들어 관리합니다. 

# https://www.studyin.co.kr/ => A
# https://www.studyin.co.kr/offline/ => B
# https://www.studyin.co.kr/offline/1 => B
# https://www.studyin.co.kr/offline/100 => B
# https://www.studyin.co.kr/online => C

################################

# Terminal에서 Ctrl + C 눌러서 서버를 종료시켜 주세요! => 우리 서비스는 작동되지 않습니다!
# 아래 명령어는 main이라는 앱을 하나 만들겠다는 것입니다. 기획이 되어 있는 상태에서는 이 명령어를 수십번 쳐서 세팅하고 들어갑니다.
python manage.py startapp main     # 메인 페이지
python manage.py startapp blog     # 게시판
python manage.py startapp accounts # 회원정보 관리, 회원정보 수정, 탈퇴 같은 것을 관리

# 아래 명령어는 사용가능하지 않습니다.
# python manage.py startapp main blog accounts

################################
# tutorialdjango > settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "blog",
    "accounts",
]
################################
# URL 구조 작성(기획 단계), 문서입니다. 
# 다른 곳에 작성하는 것이 아닙니다.

www.hojun.com/
www.hojun.com/about
www.hojun.com/contact
www.hojun.com/accounts/login
www.hojun.com/accounts/logout
www.hojun.com/blog
www.hojun.com/blog/1
www.hojun.com/blog/2
www.hojun.com/blog/3

# 테이블 형태로 한 번 정리하고 가시는 것을 권해드립니다.
# 있어야 하는 항목: URL, views 함수 이름, html 파일 등이 컬럼으로 있어야 합니다.

################################

startproject로 만든 것은 urls.py가 자동으로 생성

startapp으로 만든 앱들은 urls.py가 자동으로 생성되지 않음
따라서 urls.py를 각각 앱마다 생성해줘야한다.

main > urls.py
blog > urls.py
accounts > urls.py

질문: accounts, blog. main을 앱이라 하시는데 여기서 앱이라는게 정확히 어떤 것인지 궁금합니다
여기서 앱이란 -> 어떤 URL 묶음을 처리하기 위한 코드 묶음

################################

# URL 분기 방법!(나누는 법)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls')), # 해당 URL로 들어오면 main앱에 urls.py를 참고하겠다! => main > urls.py로 연결하는 것! 
    path("blog/", include('blog.urls')), # 해당 url로 들어오면 blog앱의 urls.py롤 사용하겠다.
    # path("blog/<int:pk>/", blogdetails), # 이것은 여기서 처리하지 않고 blog앱에 urls.py에서 처리하면 됩니다! => 즉 blog/ 처럼 blog후 / 되어 경로를 사용하는 것들은 전부 blog > urls.py에서 처리한다.
    # 여기서 처리하지 않고 blog앱에 urls.py에서 처리하면 됩니다!
    # path("blog/1", blog1) # 기존에는 이렇게 처리했는데
    # path("blog/1", blog2) # include()를 통해 해당 앱에서 처리하도록 해당 경로를 해당 앱의 urls.py을 연결
    # path("blog/1", blog3) # 이런 경로들의 내용들은 blog > urls.py에서 처리하는것(include로 blog 경로로 들어오는 것들은 blog의 urls.py에서 처리하도록 설정함)

    path("accounts/", include('accounts.urls')),
]

################################

# main > urls.py

from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path("", index),
    path("about/", about),
    path("contact/", contact),
]

################################

# main > views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def about(request):
    return HttpResponse("about")


def contact(request):
    return HttpResponse("contact")


################################
# blog > urls.py
from django.urls import path
from .views import blog, blogdetails

urlpatterns = [
    path("", blog),
    path("<int:pk>/", blogdetails),
]

################################
# blog > views.py

from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("Blog Page")


def blogdetails(request, pk):
    return HttpResponse(f"Blog Details Page: {pk}")

################################
# accounts > urls.py

from django.urls import path
from .views import login, logout

urlpatterns = [
    path("login/", login),
    path("logout/", logout),
]

################################
# accounts > views.py
from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("Login Page")


def logout(request):
    return HttpResponse("Logout Page")

################################


```