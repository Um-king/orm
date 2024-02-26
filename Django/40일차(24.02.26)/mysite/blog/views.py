from django.shortcuts import render
from django.db.models import Q

from .models import Post
from .forms import PostForm # form.py 호출 -> 입력한 값을 사용하기 위해
from django.shortcuts import redirect, get_object_or_404

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
    # # is_valid(): 유효성 검사 -> ex)로 CharField에 max_length가 20이면 해당 유효성 검사를 실시, 없어도 설정된 필드에 들어가는 타입이 맞는지 확인한다.
    # # .save()를 해야 DB에 반영된다.

    # if request.method == "GET":
    #     # print("GET으로 들어왔습니다!")
    #     form = (
    #         PostForm()
    #     )  # 이렇게 생성된 form은 자동으로 form을 만들어주는 기능을 가지고 있습니다.
    #     # 이렇게 안하면 일일이 form을 하나씩 만들어야 합니다. 이해하긴 일일이 만드는 것이 더 좋을 수도 있습니다.
    #     context = {"form": form}
    #     return render(request, "blog/blog_create.html", context)
    # elif request.method == "POST":
    #     # print("POST로 들어왔습니다!")
    #     # print(request.POST)
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         # form.is_valid()를 통과하면 form.cleaned_data를 통해 데이터를 가져올 수 있습니다. form.is_valid() 이걸 안하면 form.cleaned_data 사용할 수 없습니다. 호출도 불가합니다!
    #         # print(form)
    #         # print(form.data)
    #         # print(form.cleaned_data["title"])
    #         # print(type(form))
    #         # print(dir(form))
    #         # """
    #         # 'add_error', 'add_initial_prefix', 'add_prefix', 'as_div', 'as_p', 'as_table', 'as_ul', 'auto_id', 'base_fields', 'changed_data', 'clean', 'cleaned_data', 'data', 'declared_fields', 'default_renderer', 'empty_permitted', 'error_class', 'errors', 'field_order', 'fields', 'files', 'full_clean', 'get_context', 'get_initial_for_field', 'has_changed', 'has_error', 'hidden_fields', 'initial', 'is_bound', 'is_multipart', 'is_valid', 'label_suffix', 'media', 'non_field_errors', 'order_fields', 'prefix', 'render', 'renderer', 'template_name', 'template_name_div', 'template_name_label', 'template_name_p', 'template_name_table', 'template_name_ul', 'use_required_attribute', 'visible_fields'
    #         # """
    #         return render(request, "blog/blog_create.html")
    #     else:
    #         context = {"form": form}
    #         return render(request, "blog/blog_create.html", context)

    if request.method == "GET":
        form = PostForm()
        context = {"form": form}
        return render(request, "blog/blog_create.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES) # request.FILES: 이미지 업로드를 위한 코드
        if form.is_valid():
            post = form.save()
            # detail로 가야한다!
            # return redirect('blog_details', pk=post.pk) # post 이용
            return redirect("blog_list")
        else:
            context = {
                "form": form,
                "error": "입력이 잘못되었습니다. 알맞은 형식으로 다시 입력해주세요!",
            }
            return render(request, "blog/blog_create.html", context)


def blog_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_details", pk=post.pk)
    else:
        form = PostForm(instance=post)
        context = {"form": form, "pk": pk}
        return render(request, "blog/blog_update.html", context)


def blog_delete(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    print(post)
    if request.method == "POST":
        post.delete()
    return redirect("blog_list")