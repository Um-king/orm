# 목표
1. 아주 간단한 DB를 다뤄봅니다.
2. 데이터베이스는 각각 생성한 앱의 models.py에서 작성합니다.

# django 
* 가상환경 venv 폴더는 로컬의 하드디스크도 많이 차지함으로 그냥 삭제하는 것을 추천함
* 수업이 끝나면 삭제
* 해당 수업 내용이 보고 싶으면 다시 설치

# 가상환경 나가는것
: deactivate

# window에서 오류가 뜰 경우
Set-ExecutionPolicy Unrestricted


```python
python --version
mkdir mysite
cd mysite
python -m venv venv
.\venv\Scripts\activate # window
pip install django
django-admin startproject tutorialdjango .
python manage.py migrate
python manage.py runserver

python manage.py startapp main
python manage.py startapp blog

터미널에 해당 명령어를 전체 복사하고 붙여넣어도 알아서 반영됨
붙여넣기는 shift-insert 누르면 된다.

################################

# tutorialdjango > settings.py

ALLOWED_HOSTS = ["*"] 

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main", 
    "blog", 
]

################################
# URL 구조 작성(기획 단계), 문서입니다. 
# 연습할 때에도 이걸 만들어 놓고 연습하시기를 권고합니다 

''
'about/'
'contact/'
'blog/'
'blog<int:pk>/'


앱이름: main
URL             views 함수이름     html 파일이름        비고
''              index           index.html
'about/'        about
'contact/'      contact

앱이름: blog
URL             views 함수이름   html 파일이름      비고
'blog/'         blog            blog.html    
'blog/<int:pk>' post            post.html          게시물이 없을 경우에는 404로 연결

################################

# tutorialdjango > urls.py 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("blog/", include("blog.urls")),
]

################################

# main > urls.py

from django.urls import path
from . import views # from . 은 현재폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]

# name이 있는 이유는 이 URL의 고유 별칭입니다.
# 템플릿 같은 곳에서 이 별칭을 이용해 이 URL에 접근할 수 있습니다.

################################

# main > views.py 

from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

################################

# tutorialdjango > settings.py
# 기본 템플릿 폴더를 변경해서 앞으로는 mysite > templates

# 이제 html 파일들을 각각의 앱에서 관리하는 것이 아니라 mysite > templates에 모아서 관리를 한다.
# DIRS의 기본 경로를 변경하여 html을 호출 할 수 있도록 설정

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # 기본 템플릿 폴더 경로를 설정 -> 해당 경로에서 템플릿 파일들을 관리하겠다고 선언 -> 기본 경로 설정
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

################################

>>> from pathlib import Path
>>> file_path = './path/to/file'
>>> p = Path(file_path)
>>> p / 'templates/'
>>> p / 'templates/' / 'helloworld'

################################

# 아래 파일들 생성

templates > main > index.html
templates > main > about.html
templates > main > contact.html

################################

# main > urls.py

from django.urls import path
from . import views # from . 은 현재폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"), # name을 작성하는 것이 좋고 html에서 url 찾을 때 해당 name을 찾음
]

################################

# main > views.py

from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

################################

# 아래 파일들 생성

templates > blog > blog_list.html
templates > blog > blog_detail.html

################################

# blog > urls.py

from django.urls import path
from . import views # from . 은 현재폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]

################################

# blog > views.py

# 첫번째
from django.shortcuts import render


def blog_list(request):
    return render(request, "blog/blog_list.html")


def blog_detail(request, pk):
    return render(request, "blog/blog_detail.html")


# 두번째
blog_database = [
    {
        "id": 1,
        "title": "제목1",
        "content": "내용1",
        "created_at": "2021-02-22",
        "updated_at": "2021-02-22",
        "author": "홍길동",
        "category": "일상",
        "tag": ["태그1", "태그2"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 3,
        "like_user": [10, 20, 21],
    },
    {
        "id": 2,
        "title": "제목2",
        "content": "내용2",
        "created_at": "2021-02-23",
        "updated_at": "2021-02-23",
        "author": "김철수",
        "category": "일기",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 10,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 3,
        "title": "제목3",
        "content": "내용3",
        "created_at": "2021-02-24",
        "updated_at": "2021-02-24",
        "author": "이영희",
        "category": "맛집",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 20,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 4,
        "title": "제목4",
        "content": "내용4",
        "created_at": "2021-02-25",
        "updated_at": "2021-02-25",
        "author": "박민수",
        "category": "여행",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 30,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    }
]

def blog_list(request):
    # blogs = Blog.objects.all() # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"blog_list": blog_database}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk) # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"blog": blog_database[pk - 1]}
    return render(request, "blog/blog_detail.html", context)


################################

python manage.py runserver

################################
# templates 폴더를 별도로 만들어서 html을 통합 관리하고 있다.
# templates > blog > blog_list.html

{# url은 urls.py의 name, id는 pk 즉 파라미터 값(파라미터의 개수만큼 추가 할 수 있음, id는 blog/1 경로 처럼 1의 값이 pk가 되고 blog.id는 1) #}

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <h1>bloglist</h1>
    <ul>
        {% for blog in blog_list %}
        <li>
            {# 주석입니다. 'url 'blog_detail' blog.id' 와 같은 형태는 urls.py에서 blog_detail이라는 name을 가진 url을 찾습니다. 그걸로만 연결을 해주는데 뒤에 값이 들어가야 할 경우, 파라미터가 있는 경우! 뒤에 띄어쓰기로 아규먼트를 넣어줄 수 있습니다. 결국에는 blog.id가 blog_detail에 pk로 들어가는 것입니다. #}
            <a href="{% url 'blog_detail' blog.id %}">{{ blog.title }}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>

            
# <a href="{% url 'blog_detail' blog.id %}">{{ blog.title }}</a> 이렇게 사용하지 않고
# <a href="blog/{{blog.id}}">{{ blog.title }}</a> 이렇게 작성하는 경우도 많다
# 이렇게 코딩하는 것은 하드코딩이라고 한다
# 다만 이렇게 코딩하면 유지보수성이 떨어집니다! 그래서 실무에서는 이런 하드코딩 패턴을 피해야 합니다.

################################

# templates > blog > blog_detail.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>blogdetail</title>
</head>
<body>
    <h1>blogdetail</h1>
    <h2>{{ blog.title }}</h2>
    <p>{{ blog.content }}</p>
    <p>{{ blog.created_at }}</p>
    <p>{{ blog.updated_at }}</p>
    <a href="{% url 'blog_list' %}">목록</a>
</body>
</html>

################################

# 템플릿 상속!!!!!
# 템플릿 문법 숙지해야한다..! -> 볼렛 만들고 숫자가 있는 li만들고 이런거

################################
################################
################################
################################
################################



```