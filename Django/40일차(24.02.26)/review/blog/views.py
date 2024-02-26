from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm

def blog_list(request):
    if request.GET.get("q"): # request 객체로 넘어온, request 객체가 가지고 있는 내용 중 q라는 key에 값이 있다면
        db = Post.objects.filter(
            Q(title__contains=request.GET.get("q")) # 여기서 Q객체를 사용해야 최적화가 가능
            | Q(contents__contains=request.GET.get("q"))  # contains -> DB에 해당 내용의 컨텐츠가 포함되어 있는지 확인 즉 title_contains와 contents_contains를 사용하면 DB에 title과 contents 필드에 해당 값이 포함되어 있는 것을 전부 호출한다.
        ).distinct()
    else:
        db = Post.objects.all()
    context = {"db": db}
    return render(request, "blog/blog_list.html", context)


def blog_details(request, pk):
    db = Post.objects.get(pk=pk)
    context = {"db": db}
    return render(request, "blog/blog_details.html", context)


def blog_create(request):
    if request.method == "GET":
        form = PostForm()
        context = {"form": form}
        return render(request, "blog/blog_create.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # detail로 가야한다!
            # return redirect('blog_details', pk=post.pk)
            return redirect("blog_list")
        else:
            context = {"form": form}
            return render(request, "blog/blog_create.html", context)

def blog_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # post의 자리를 찾아내서 instance에 덮어쓴다 -> 이렇게 update 되는것(원래는 id값을 찾아서 get으로 값을 가져와서 객체에 할당 후 save()를 해야하는데 PostFor()을 통해 해당 post 객체의 값을 알아서 저장해주는 것)
        # 원래는 request.GET.get('객체명') 해서 값을 가져와서 새로운 변수에 할당하고 .save()로 DB에 반영했는데
        # PostForm()을 통해 request객체에서 해당 pk 값에 해당하는 post 객체를 찾고 post객체의 값을 알아서 인스턴스의 필드에 연결
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_details", pk=post.pk)
    else: # request method가 Get일 경우
        # form 태그로 Post,Get이 사용된 것 아닌 이상, 우리가 버튼을 눌러서 페이지가 이동한 것은 전부 Get방식이다.
        form = PostForm(instance=post)
        context = {"form": form, "pk": pk}
        return render(request, "blog/blog_update.html", context)


# @login_required : 선언하면 로그인한 작성자만 지울 수 있다.
def blog_delete(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    print(post)
    if request.method == "POST":
        post.delete()
    return redirect("blog_list")