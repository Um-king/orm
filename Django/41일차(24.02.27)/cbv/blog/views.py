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

# 클래스 기반 뷰가 꼭 제네릭 뷰는 아닙니다.
# 클래스로 HttpResponse를 반환하게 하면 그것도 클래스 기반 뷰입니다.
# 실무에서는 클래스 기반 뷰를 제네릭 뷰라고 부르는 경우가 많습니다.
# 제네릭 뷰는 장고에서 제공하는 여러가지 기능을 미리 구현해 놓은 클래스 기반 뷰입니다.


# model = Post : DB 연결(Post가 DB 내용, model에 할당)


class PostList(ListView): # BlogList class는 ListView를 상속 받음
    model = Post # Post 객체를 통해 DB내용을 model과 연결
    ordering = "-pk" # 내림차순 정렬, 기본 값은 최신 게시물이 DB상엔 맨 아래에 저장되므로 역순으로 정렬하고 최신 저장 내용을 가져와 출력
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html
    
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_list.html로 설정되므로 내가 변경하려면 사용하지만 선언안하면 기본값 사용 => 여기에 내가 연결할 템플릿경로를 작성하면된다.(해당 url로 들어오는 것에 대한 html 파일을 연결하는 것)
    # template_name을 설정안하면 기본값으로 해당 PostList가 출력하는 템플릿 페이지는 blog/post_list.html이다. 따라서 post_list.html을 만들면됨
    # blog/post_list.html를 생성하지 않았다면 template_name을 작성해줘야한다 template_name = blog/blog_list.html
    # template_name 선언 안하면 해당 경로 접속시 기본값으로 blog/post_list.html를 찾고 선언하면 선언한 html파일을 찾느나.

    def get_queryset(self): # queryset이란 데이터베이스에서 값 요청이 온 것
        queryset = super().get_queryset() # 여기서 super는 PostList 자체

        # request에서 GET 파라미터 q를 가져옴
        q = self.request.GET.get('q', '') # q는 post_list.html의 input tag 중 name = 'q' 즉 q의 input tag에 작성된 값을 확인
        if q: # 입력받은 q의 값이 존재한다면
            queryset = queryset.filter(Q(title_icontains=q) | Q(content_icontains=q)).distinct() 
        return queryset

class PostDetail(DetailView): # import한 DetailView 상속
    model = Post # Post는 DB데이터, DB데이터를 model에 연결하여 실제 출력 페이지에 반영하는 것
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_detail.html
    
class PostCreate(CreateView):
    model = Post # 이런식으로 반드시 DB와 model을 연결해줘야한다.
    fields='__all__' # DB의 모든 컬럼을 가져온다
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html
    success_url=reverse_lazy('blog_list')
    # reverse_lazy('blog_list') 하는 이유는 object가 생성되고 나서 url로 이동해야하는데 reverse함수는 함수이기 떄문에 함수가 실행되는 시점에 url로 바로 이동하게 되어버린다.
    # 그래서 post가 생성된 후에 url로 이동하게 하기 위해서 기다리겠다는 함수가 reverse_lazy를 사용한다.
    # 즉 DB가 연결되고 반영되었다는 신호가 오면 해당 url로 이동하겠다는 것(비동기식이기 때문에 DB와 연결되고 반영되었다는 신호와 함수가 별개로 수행되고 DB 연결이 되기전에 함수가 실행되면 url로 이동한다)
    # 따라서 Post의 DB내용과 모델이 연결될 때까지 기다렸다가 정상적으로 연결되었다면 reverse_lazy 함수를 통해 해당 url로 이동하는 것(절대 reverse() 함수 사용x -> 안기다리고 바로url이동함)

class PostUpdate(UpdateView):
    model = Post 
    fields='__all__'
    success_url=reverse_lazy('blog_list')
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html


class PostDelete(DeleteView):
    model = Post 
    success_url=reverse_lazy('blog_list') # 삭제되고 다 완료되지 않은 상태에서 blog_list로 넘어가지 않도록 하기 위해서 reverse_lazy를 사용합니다.
    # 즉 삭제가 다 완료되었다고 연결된 DB에서 확인이 되면 확인이 될때까지 기다렸다가 성공적으로 삭제되고 DB에 반영되었다면
    # blog_list의 해당 url로 이동하겠다는 것(reverse_lazy() 사용해야한다.)
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_confirm_delete.html


class PostTest(CreateView):
    model = Post

    # 이렇게 재정의 하는 것을 메서드 오버라이딩이라고 합니다.
    # 이렇게 재정의 하는 것을? 매서드 오버라이딩이라고 합니다.
    def get(self, request):
        return HttpResponse("get 요청이 왔습니다.")

    def post(self, request):
        return HttpResponse("post 요청이 왔습니다.")


# 실무에서는 바로 as_view()를 붙여서 사용합니다.
# urls의 패턴을 우리가 배운 형태되로 유지하기 위해서 아래처럼 사용하겠습니다.
blog_list = PostList.as_view()
blog_details = PostDetail.as_view()
blog_write = PostCreate.as_view()
blog_edit = PostUpdate.as_view()
blog_delete = PostDelete.as_view()
test = PostTest.as_view()
# 즉 urls.py에서 접속된 경로에서 views.blog_list를 호출하면 해당 views.py에서 위의 코드처럼 class를 정의하고 해당 변수에 as_view()를 통해 할당하고 실행한다.
# 만약 url을 blog/로 접속하면 urls.py에 "" 경로로 접속하게 되고 views.blog_list를 호출한다.
# 그럼 views.py에서 확인할때 blog_list의 작성내용을 보고 blog_list는 as_view()를 통해 PostList.as_view()를 할당했고 PostList class 객체가 할당된것
# 따라서 PostList class와 연결된 템플릿 페이지를 출력하게 된다.