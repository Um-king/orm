# 장고에서 리스트뷰를 사용하고 싶어? 그럼 ListView를 사용하세요 처럼 애초에 List 출력하는 페이지에 대한 기본 셋팅을 제공해준다.
# 즉 우리가 만들려던 CRUD 페이지 구현을 기본적으로 제공해준다. -> 호출해서 사용만 하면 된다(그전처럼 직접 태그를 작성해서 구현하지 않음)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render



class PostList(ListView): 
    model = Post 
    ordering = "-pk" 
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: tube/post_list.html
    
    # context로 object_list가 사용됨 -> object_list라는 객체가 기본적으로 사용되는 객체 명인지? -> 강사님은 posts라는 변수로 인수로 전달해서 사용
    # 나는 인수로 전달한적이 잆는데 object_list라는 객체명은 어떻게 호출한건지
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '')

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q)).distinct()
        return queryset
    

class PostDetail(DetailView): 
    model = Post 
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_detail.html
    

class PostCreate(CreateView):
    model = Post
    fields='__all__' 
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html
    success_url=reverse_lazy('blog_list')


class PostUpdate(UpdateView):
    model = Post 
    fields='__all__'
    success_url=reverse_lazy('blog_list')
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html


class PostDelete(DeleteView):
    model = Post 
    success_url=reverse_lazy('blog_list')
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_confirm_delete.html


def tube_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "tube/post_list.html", {"object_list": posts})


blog_list = PostList.as_view()
blog_details = PostDetail.as_view()
blog_create = PostCreate.as_view()
blog_update = PostUpdate.as_view()
blog_delete = PostDelete.as_view()




































