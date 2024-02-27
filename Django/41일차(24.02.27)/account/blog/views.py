from django.shortcuts import render
from .models import Post


# 목록을 출력하는 것들에서는 Post.objects.함수()를 통해 db 내용을 불러와야한다.!

# @login_required: 로그인한 사용자만 보여지도록 하겠다.
def blog_list(request):
    blogs = Post.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog/blog_list.html", context)

# 수정작업은 현재 로그인한 사용자와 request의 사용자가 같다면 수정기능이 가능하도록 한다.


def blog_details(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {"blog": blog}
    return render(request, "blog/blog_detail.html", context)