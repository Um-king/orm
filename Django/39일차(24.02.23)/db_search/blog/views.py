from django.shortcuts import render
from .models import Post
from django.db.models import Q


def blog_list(request):
    # blog_list의 검색하기를 누르면 검색 내용이(input에 작성한 내용) request에 담긴다.
    if request.GET.get('q'): # q는 input 태그의 name -> 즉 request 객체에 name=q 라는 내용이 있는지
        q = request.GET.get('q')

        # 즉 input 태그 중 q의 값을 filter를 통해 title과 contets 필드중에 해당 값이 존재하면 해당 값을 전부 출력
        # input 태그에 값을 1로 하면 title과 contents 필드에 1이란 값을 전부 호출한다.(like %'1'%)
        # 따라서 1, 11, 111, 111..... 1이 포함된 모든 데이터가 출력된다.
        db = Post.objects.filter(Q(title_icontains=q) | Q(contents_icontains=q)) # title 과 contents의 내용에서 q의 내용이 있는지 확인한다.

    else:
        db = Post.objects.all()
    context = {
        "db": db,
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        "db": db,
    }
    return render(request, "blog/blog_detail.html", context)