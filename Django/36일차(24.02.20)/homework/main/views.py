from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def notice(request):
    return render(request, "main/notice/index.html")

def notice1(request):
    return render(request, "main/notice/1.html")

def notice2(request):
    return render(request, "main/notice/2.html")

def notice3(request):
    return render(request, "main/notice/3.html")

def contact(request):
    return render(request, "main/contact.html")

def d(request):
    return render(request, "main/a/b/c/d.html")

def hojun(request):
    return render(request, "main/user/hojun.html")

def mini(request):
    return render(request, "main/user/mini.html")


# 이러면 notice가 100라면 100가의 함수를 정의해야함으로 urls.py에서 동적으로 생성된 내용에서 인덱스 값을 변수로 받는다.
# def notice1(request):
#     return render(request, "main/notice/1.html")

# def notice2(request):
#     return render(request, "main/notice/2.html")

# def notice3(request):
#     return render(request, "main/notice/3.html")



# blog_data = {
# 1: test1,
# 2: test2
# }
# 이런식으로 작성된 내용과 함께 html을 생성함
# urls.py에서 pk 값을 받을 수 있음 -> url 입력 할때 notice/1 이렇게 경로를 입력하면 1이 pk 값으로 사용됨
# def notice(request, pk):
#     print(blog_data[pk])
#     return render(request, "main/notice.html")
