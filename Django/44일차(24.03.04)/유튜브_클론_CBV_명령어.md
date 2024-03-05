youtube를 클론하는 프로젝트를 하고 있습니다. 참고로 영상은 file입니다. 다음 프로젝트를 완성하세요.

1. 작동되는 models.py를 각 반에 업로드 하세요.
2. 작동되는 views.py를 각 반에 업로드 하세요.

/tube   
/tube/1                     # 영상 재생이 되어야 합니다. 뎃글을 달 수 있어야 합니다.
/tube/create/               # 로그인한 사용자만 보기 가능
/tube/update/<int:pk>/      # 로그인한 사용자만 보기 가능
/tube/delete/<int:pk>/      # 로그인한 사용자만 보기 가능
/tube/tag/<str:tag>/        # 해당 태그가 달린 목록을 가져와야 합니다.
/tube/?q='keyword'          # 해당 키워드가 포함된 title, content가 있는 목록을 가져와야 합니다.
/accounts/signup/
/accounts/login/
/accounts/logout/           # 로그인한 사용자만 보기 가능
/accounts/profile/          # 로그인한 사용자만 보기 가능

```python
mkdir 0304
cd 0304
mkdir mysite
cd mysite

pip freeze > requirements.txt
# pip install -r requirements.txt # 추후 이 파일을 통해 설치합니다.

django-admin startproject tutorialdjango .
python manage.py migrate

# settings.py에서 접속할 수 있는 사람 설정
ALLOWED_HOSTS = ['*'] # 28번째 줄에 접속할 수 있는 사람을 모든 사람으로 변경

python manage.py startapp tube
python manage.py startapp accounts


###################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'accounts',
    'tube',
]

###################################

'DIRS': [BASE_DIR / 'templates'],

###################################

# 언어와 시간 설정
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
###################################

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

###################################

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

###################################

static 폴더 생성
media 폴더 생성
templates > tube 폴더 생성
templates > accounts 폴더 생성

###################################

python manage.py createsuperuser
leehojun
leehojun@gmail.com
이호준123!@

###################################
# tutorialdjango > urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tube/', include('tube.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###################################
# tube > urls.py

from django.urls import path
from . import views

urlpatterns = []

###################################
# accounts > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile')
]

###################################
# accounts > views.py
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

# 모든 cbv가 form 자동 생성

# 클래스 형태로 사용 => 기본으로 제공하는 Form을 사용
signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = '/accounts/login/'
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

logout = LogoutView.as_view(
    next_page = '/accounts/login/'
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
###################################
# templates > accounts > form.html

<form action="" method="post" enctype="multipart/form-data"> # enctype="multipart/form-data": 이미지나 파일을 같이 올릴때 사용하는 메서드(프로필 이미지)
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="Submit">
</form>
###################################
# templates > accounts > profile.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>프로필</title>
</head>
<body>
    <h1>프로필 페이지입니다.</h1>
    <p>{{user}}의 프로필 페이지입니다.</p>
</body>
</html>

###################################

runserver 후에 login, logout이 되는지 확인

###################################
# tube > models.py

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumb_image = models.ImageField(
        upload_to='tube/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='tube/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/tube/{self.pk}/'
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.message
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

###################################

python manage.py makemigrations
python manage.py migrate

###################################

from django.contrib import admin
from .models import Post, Comment, Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)

###################################

notion : https://paullabworkspace.notion.site/sample-assets-b7de17d3108145659216619aa82dc327?pvs=4
asset 다운로드 후 admin으로 게시물 3개 업로드

###################################
# tube > forms.py
from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__' # 이렇게 사용하는것은 안좋다 -> 프로젝트 진행할때 마이너스 요소 밑에 필드로 가져오기
        fields = ['title', 'content', 'thumb_image', 'file_upload'] # counter같은 값은 건들면 안되니까!


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


###################################
tube > urls.py

from django.urls import path
from . import views

app_name = 'tube' # app name 지정

# {% url 'tube:post_list' %}
# {% url 'tube:post_detail' post.pk %}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
]

###################################
tube > views.py

from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list') # reverse_lazy로 사용해야한다 : 지연을 시키고 해당 페이지로 이동. 함수를 실행하고 있는 도중에 html 페이지로 이동하면 안되니깐 함수 실행이 완료되면 다음 행동을 수행하겠다.
    template_name = 'tube/form.html'

post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post

post_detail = PostDetailView.as_view()


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

post_edit = PostUpdateView.as_view()


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

post_delete = PostDeleteView.as_view()

###################################
# tutorialdjango > urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url='tube/'), name='root'),
    path('', RedirectView.as_view(pattern_name='tube:post_list'), name='root'), # RedirectView.as_view: tube의 post_list로 보내주겠다 main으로 연결되어도 바로 post_list 페이지로 이동시켜주는 것
    path('admin/', admin.site.urls),
    path('tube/', include('tube.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###################################
# tube > form.html

<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit" value="Submit">
</form>

###################################
# tube > post_confirm_delete.html

<h1>글 삭제</h1>

<form method="post">
    {% csrf_token %}
    <p>글을 삭제하시겠습니까?</p>
    <input type="submit" value="네!" class="btn btn-primary">
</form>

###################################
# tube > post_detail.html

<p>{{post.title}}</p>
<p>{{post.content}}</p>
{% if post.file_upload %}
<video src="{{post.file_upload.url}}" controls></video>
{% endif %}

<hr>

<a href="{% url 'tube:post_list' %}">목록</a>
{% if user == post.author %}
<a href="{% url 'tube:post_edit' post.pk %}">수정</a>
<a href="{% url 'tube:post_delete' post.pk %}">삭제</a>
{% endif %}

###################################
# tube > post_list.html
<ul>
    {% for post in post_list %}
    <li>
        <a href="{% url 'tube:post_detail' post.pk %}">
            {{ post.title }}
        </a>
    </li>
    {% endfor %}
</ul>
<a href="{% url 'tube:post_new' %}">업로드</a>
###################################
# tube > views.py

# write는 로그인 해야만
# update와 delete는 업로드한 사용자여야만

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView): # LoginRequiredMixin: 로그인한 사용자만 생성 가능
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def form_valid(self, form):
        video = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        video.author = self.request.user
        return super().form_valid(form) # 이렇게 호출했을 때 저장합니다.

post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user 
        # UserPassesTestMixin를 사용하면 무조건 test_func함수를 정의해야한다(함수명이 test_func()으로 정해져있고 오버라이딩하는 것)


post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()

###################################
믹스인 정리
공식 문서: https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins/

인증 관련 믹스인:
LoginRequiredMixin: 사용자가 로그인 되어 있을 경우에만 뷰에 접근을 허용합니다.
PermissionRequiredMixin: 사용자에게 특정 권한이 있을 경우에만 뷰에 접근을 허용합니다.
UserPassesTestMixin: test_func() 메서드를 오버라이드하여 사용자가 특정 테스트를 통과할 경우에만 뷰에 접근을 허용합니다.

폼 관련 믹스인:
FormMixin: 폼과 관련된 기본 기능 (폼 인스턴스 생성, 폼 데이터 저장 등)을 제공합니다.
ModelFormMixin: 모델 폼과 관련된 작업에 필요한 메서드를 제공합니다.

리스트 뷰 관련 믹스인:
MultipleObjectMixin: 여러 객체를 처리하는 뷰 (예: 리스트 뷰)에 공통적으로 사용되는 메서드나 속성을 제공합니다.
SingleObjectMixin: 단일 객체를 처리하는 뷰에 필요한 메서드나 속성을 제공합니다.

페이징 관련 믹스인:
MultipleObjectPaginationMixin: 여러 객체를 페이지 단위로 표시하기 위한 페이징 처리 기능을 제공합니다.

상세 뷰 관련 믹스인:
SingleObjectMixin: 단일 객체에 대한 상세 정보를 제공하는 뷰에서 사용되는 메서드와 속성을 제공합니다.

기타 믹스인:
ContextMixin: 컨텍스트 데이터를 뷰에 추가하는 메서드를 제공합니다.
TemplateResponseMixin: 템플릿을 사용하여 응답을 생성하는 메서드를 제공합니다.
RedirectView: 뷰를 다른 URL로 리다이렉트하는 기능을 제공합니다.


###################################
# post_detail.html에서 둘 다 접근 가능
# object.title, post.title

<p>{{object.title}}</p>
<p>{{object.content}}</p>

<p>{{post.title}}</p>
<p>{{post.content}}</p>
{% if post.file_upload %}
<video src="{{post.file_upload.url}}" controls></video>
{% endif %}

<hr>

<a href="{% url 'tube:post_list' %}">목록</a>
{% if user == post.author %}
<a href="{% url 'tube:post_edit' post.pk %}">수정</a>
<a href="{% url 'tube:post_delete' post.pk %}">삭제</a>
{% endif %}

###################################
# 댓글 작성되게 하기


# 전달되는 context 조정
# views.py
class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        PostDetailView를 하는데 Post에 DB내용이 담겨져 있다 model = Post Post DB내용을 model에 연결하겠다.
        get_context_data()를 통해 DB내용을 가져오는 것 즉 model = Post를 하기 위해 def get_context_data(self, **kwargs) 함수를 오버라이딩하여 정의한 후 context에 DB 내용을 담는다. => 해당 페이지에 반환값으로 DB내용이 저장된 context를 전달하는 것
        '''
        context = super().get_context_data(**kwargs) # get_context_data: context에 쿼리를 추가하는것 => 기본적으로 가지고 있는 쿼리셋으로 PostDetailView는 DetailView의 Model을 상속하고 있으니깐 Detail Model의 내용을 가져오는것
        print('------------')
        print(kwargs) # 각각 무엇을 포함하고 있는지 확인하여 해당 명들을 통해 호출할 수 있음 -> post라는 객체가 담겨져 있다.
        print(context)
        print(type(context))
        print(dir(context))
        print('------------')
        return context

post_detail = PostDetailView.as_view()


# 원래 했던 blog 코드
# def blog(request):
#     # db = Blog.objects.all()
#     # db2 = Blog.objects.all().order_by('-id')[:3] 이런식으로 DB 내용을 호출
#     context = { # 그다음 변수에 해당 객체를 할당하여 전달
#         'db': db,
#         'db2' : db2, ... # 원하는 만큼 전달 가능
#     }
#     return render(request, 'blog/blog.html', context)


###################################
# views.py

class PostDetailView(DetailView):
    model = Post # object로 접근하던걸 Post로 접근하는 것.
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm() # 이렇게 추가할 수도 있다 -> comment_form이라는 이름으로 CommentForm의 내용을 담겠다.
        return context

post_detail = PostDetailView.as_view()


###################################
# post_detail.html

<p>{{object.title}}</p>
<p>{{object.content}}</p>

<p>{{post.title}}</p>
<p>{{post.content}}</p>
{% if post.file_upload %}
<video src="{{post.file_upload.url}}" controls></video>
{% endif %}

<hr>
<section>
    <h3>댓글</h3>
    {% for comment in post.comments.all %} # post.comments -> context = super().get_context_data(**kwargs)
        <p>{{comment.message}}</p>
        <p>{{comment.author}}</p>
        <p>{{comment.updated_at}}</p>
    {% endfor %}
</section>

<section>
    <h3>댓글 작성</h3>
    <form action="#" method="post">
        {% csrf_token %}
        {{ comment_form.as_p }} # context['comment_form'] = CommentForm()의 내용
        <input type="submit" value="댓글 작성">
    </form>
</section>

<a href="{% url 'tube:post_list' %}">목록</a>
{% if user == post.author %}
<a href="{% url 'tube:post_edit' post.pk %}">수정</a>
<a href="{% url 'tube:post_delete' post.pk %}">삭제</a>
{% endif %}

###################################

댓글 leehojun으로 1 ~ 2개
댓글 hello로 1 ~ 2개 

업로드 해서 댓글이 보이는지 확인 필요!

###################################

# post_detail.html

<p>{{object.title}}</p>
<p>{{object.content}}</p>

<p>{{post.title}}</p>
<p>{{post.content}}</p>
{% if post.file_upload %}
<video src="{{post.file_upload.url}}" controls></video>
{% endif %}

<hr>
<section>
    <h3>댓글</h3>
    {% for comment in post.comments.all %}
        <p>{{comment.message}}</p>
        <p>{{comment.author}}</p>
        <p>{{comment.updated_at}}</p>
    {% endfor %}
</section>

<section>
    <h3>댓글 작성</h3>
    <form action="{% url 'tube:comment_new' post.pk %}" method="post">
        {% csrf_token %}
        {{ comment_form.as_p }}
        <input type="submit" value="댓글 작성">
    </form>
</section>

<a href="{% url 'tube:post_list' %}">목록</a>
{% if user == post.author %}
<a href="{% url 'tube:post_edit' post.pk %}">수정</a>
<a href="{% url 'tube:post_delete' post.pk %}">삭제</a>
{% endif %}



###################################
# views.py

# write는 로그인 해야만
# update와 delete는 업로드한 사용자여야만

from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def form_valid(self, form):
        video = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        video.author = self.request.user
        return super().form_valid(form) # 이렇게 호출했을 때 저장합니다.

post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()


@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('tube:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'tube/form.html', {
        'form': form,
    })

###################################
# 조회수 넣기
# post_detail.html

<p>{{object.title}}</p>
<p>{{object.content}}</p>

<p>{{post.title}}</p>
<p>{{post.content}}</p>
<p>조회수 : {{post.view_count}}</p>
{% if post.file_upload %}
<video src="{{post.file_upload.url}}" controls></video>
{% endif %}

<hr>
<section>
    <h3>댓글</h3>
    {% for comment in post.comments.all %}
        <p>{{comment.message}}</p>
        <p>{{comment.author}}</p>
        <p>{{comment.updated_at}}</p>
    {% endfor %}
</section>

<section>
    <h3>댓글 작성</h3>
    <form action="{% url 'tube:comment_new' post.pk %}" method="post">
        {% csrf_token %}
        {{ comment_form.as_p }}
        <input type="submit" value="댓글 작성">
    </form>
</section>

<a href="{% url 'tube:post_list' %}">목록</a>
{% if user == post.author %}
<a href="{% url 'tube:post_edit' post.pk %}">수정</a>
<a href="{% url 'tube:post_delete' post.pk %}">삭제</a>
{% endif %}



###################################
# views.py 수정

class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None): # 쿼리셋을 어떻게 할거냐 -> 요청이 왔을때 -> object를 가져오는 것
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk) # 해당 pk의 object를 가져온다.
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()

###################################
# post_list.html

<h1>Post List</h1>
<!-- 검색 기능 추가 -->
<form action="" method="GET">
    <input type="text" name="q" value="{{ request.GET.q }}">
    <input type="submit" value="검색">
</form>
<ul>
    {% for post in post_list %}
    <li>
        <a href="{% url 'tube:post_detail' post.pk %}">
            {{ post.title }}
        </a>
    </li>
    {% endfor %}
</ul>
<a href="{% url 'tube:post_new' %}">업로드</a>

###################################
# views.py

# write는 로그인 해야만
# update와 delete는 업로드한 사용자여야만

from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '') # q가있다면 q의 값을 , 없다면 '' 빈 문자열을
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostListView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def form_valid(self, form): # form의 유효성 검사를 위한 함수
        video = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
        video.author = self.request.user # 권한을 로그인한 사용자 정보로 등록
        return super().form_valid(form) # 이렇게 호출했을 때 저장합니다.

post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

    def get_context_data(self, **kwargs):
        '''
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None):
        '''
        말 그대로 PostDetailView.as_view()에서 사용할 object를 반환합니다.
        반환 하는데 object를 변경할 수 있는 함수입니다.
        여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
        '''
        pk = self.kwargs.get('pk')
        print(self.kwargs)
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')

    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()


@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('tube:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'tube/form.html', {
        'form': form,
    })

# 아래 글은 선별해서 읽어주세요.
# https://medium.com/@jongyoungpark/%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC-%EA%B3%B5%EB%B6%80%EB%A5%BC-%EB%A9%88%EC%B6%B0%EB%9D%BC-1afa37644474
# 언어
# 네트워크(http, https)
# os
# 인프라(aws)


###################################
###################################
###################################
# 나아가기: tag
# post_detail.html

<p>{{object.title}}</p>
<p>{{object.content}}</p>

<p>{{post.title}}</p>
<p>{{post.content}}</p>
<p>조회수 : {{post.view_count}}</p>
{% if post.file_upload %}
<video src="{{post.file_upload.url}}" controls></video>
{% endif %}

<hr>
<section>
    <h3>태그</h3>
    {% for tag in post.tags.all %}
        <p>{{tag.name}}</p>
    {% endfor %}
</section>

<section>
    <h3>댓글</h3>
    {% for comment in post.comments.all %}
        <p>{{comment.message}}</p>
        <p>{{comment.author}}</p>
        <p>{{comment.updated_at}}</p>
    {% endfor %}
</section>

<section>
    <h3>댓글 작성</h3>
    <form action="{% url 'tube:comment_new' post.pk %}" method="post">
        {% csrf_token %}
        {{ comment_form.as_p }}
        <input type="submit" value="댓글 작성">
    </form>
</section>

<a href="{% url 'tube:post_list' %}">목록</a>
{% if user == post.author %}
<a href="{% url 'tube:post_edit' post.pk %}">수정</a>
<a href="{% url 'tube:post_delete' post.pk %}">삭제</a>
{% endif %}


###################################
# 태그 입력 가능하게 하는 것
# forms.py
# 그럼 이 필드에 태그가 생성되게 하는 코드가 함께 있어야 합니다.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'thumb_image', 'file_upload', 'tags'] # counter같은 값은 건들면 안되니까!
```