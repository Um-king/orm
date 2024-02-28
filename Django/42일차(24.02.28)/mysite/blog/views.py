from django.shortcuts import render
from datetime import date
from .models import Post

def blog_list(request):
    # 가장 처음 실습
    posts = Post.objects.all()

    # 1. 연도와 일치되는 게시물 가져오기
    # posts = Post.objects.filter(created_at__year=2023)

    # 2. 월과 일치되는 게시물 가져오기
    # posts = Post.objects.filter(created_at__month=10)

    # 3. 일과 일치되는 게시물 가져오기
    # posts = Post.objects.filter(created_at__day=17)

    # 4. 연, 월, 일에 매칭이 되는 게시물 가져오기
    # posts = Post.objects.filter(created_at__gte=date(2023,10,17))


    context = {'posts':posts}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, "blog/blog_detail.html", {"post": post, "form": form})


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "blog/blog_list.html", {"posts": posts})