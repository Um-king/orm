from django.shortcuts import render

# HttpResponse는 주로 테스트용으로 사용합니다. 실제로는 html파일을 통해 화면에 출력합니다.
# from django.http import HttpResponse


# # tutorialdjango의 urls.py에 설정된 함수를 정의
# # 해당 url로 접속할 때 해당 url과 연결된 함수 호출을 통해 해당 URL에 보여줄 화면을 출력한다.
# def index(request):
#     return HttpResponse("<h1>메인화면 입니다!</h1>")

# def a(request):
#     return HttpResponse("<h1>a 입니다!</h1>")

# def b(request):
#     return HttpResponse("<h1>b 입니다!</h1>")

# def c(request):
#     return HttpResponse("<h1>c 입니다!</h1>")

# def hojun(request):
#     return HttpResponse("<h1>hojun 입니다!</h1>")

# def orm(request):
#     return HttpResponse("<h1>orm 입니다!</h1>")


# 실제 html 파일을 화면에 출력합니다.
def index(request):
    return render(request, "main/index.html")

def a(request):
    return render(request, "main/a.html")

def b(request):
    return render(request, "main/b.html")

def c(request):
    return render(request, "main/c.html")

def hojun(request):
    return render(request, "main/hojun.html")

def orm(request):
    return render(request, "main/orm.html")
