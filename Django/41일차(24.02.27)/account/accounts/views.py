from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# http와 render를 감추고 알아서 해주는 것
# CreateView.as_view() 가 무엇인지 확인해보기 -> CreateView.as_view()를 사용하여 코드도 짧아지고 더 빠르게 기능을 구현할 수 있다(속도도 빠름)
# -> get, post 요청에 대한 것을 고민하지말고 길게 작성되어야할 로그인 함수정의를 해당코드로 django에서 알아서 해주는 것

# "Class 기반의 View"
signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/form.html",
    success_url=settings.LOGIN_URL, # tutorialdjango > settings에 선언했음 -> 해당 경로로 이동함
)

login = LoginView.as_view(
    template_name="accounts/form.html",
    # success_url=settings.LOGIN_REDIRECT_URL,
    # next_page=settings.LOGIN_REDIRECT_URL,

    # 회원 가입 후 프로필 페이지로 넘어가지는 이유
    # 회원 가입이 성공적으로 이루어지면 LOGIN_URL 설정된 /accounts/login/ 페이지 즉 로그인 페이지로 이동한다.
    # Django에서는 회원가입이 정상적으로 이루어지면 자동 로그인 기능을 제공해주는 것 같음
    # 따라서 회원가입이후 로그인 페이지를 갔다가 자동 로그인 되고 로그인이 완료되면 프로필 페이지로 이동하게 된다.
)


logout = LogoutView.as_view(
    next_page=settings.LOGOUT_URL, # tutorialdjango > settings에 선언했음 -> 해당 경로로 이동함

      # LOGOUT_URL은 /accounts/profile/로 설정되어있고
    # 다음 페이지는 profile 페이지로 이동하게 되어 있으므로 profile() 함수를 호출
    # 하지만 profile()함수는 @login_required 설정되어있고 해당 문법은 로그인되어 있는 사용자만 접근 가능하도록 하는 것
    # 즉 로그아웃된 상태이므로 자동으로 login페이지로 이동시켜준다.
    
    # 로그아웃 후 사용자가 인증이 필요한 페이지(예: 프로필 페이지)에 접근하려고 할 때, @login_required 데코레이터가 적용된 뷰는 사용자가 로그인 상태인지 먼저 확인합니다. 로그아웃한 상태에서 이러한 페이지에 접근하려고 하면, Django는 자동으로 로그인 페이지로 리디렉션합니다. 이는 LOGIN_URL 설정을 사용하여 로그인 페이지의 URL을 지정함으로써 구현됩니다.
)


# @login_required : 로그인한 사용자인지 확인하는 문법(이렇게 작성하면 django에서 알아서 로그인한 사용자인지 확인한다.)
@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def logincheck(request):
    if request.user.is_authenticated:
        return HttpResponse("로그인 됨!")
    return HttpResponse("로그인 안됨!!")
    

def loginfbv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login 성공")
        else:
            return HttpResponse("login 실패")
    return render(request, 'accounts/loginfbv.html')





# 로그인 같은 경우는 거의 대부분 Class기반 View를 사용하기 때문에 위의 클래스 기반의 뷰 작업으로 작성


# # "함수 기반의 View"
# def signup(request):
#     pass


# def login(request):
#     pass


# def logout(request):
#     pass


# def profile(request):
#     pass