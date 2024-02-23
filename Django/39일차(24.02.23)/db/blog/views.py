# 오전 blog 예시 1
# from django.shortcuts import render
# from django.template.loader import render_to_string # 실무에서 사용x -> 원리 파악을 위해 학습하는 것
# from django.http import HttpResponse, JsonResponse
# # from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, HttpResponseForbidden


# def blog_list(request):
#     return render(request, "blog_list.html")


# def blog_test(request):
#     # request : 사용자 요청(HttpRequest)
#     # response : 서버의 응답(HttpResponse)
#     data = [
#             {'title': 'Post 1', 'text': 'Text 1', 'pk': 1},
#             {'title': 'Post 2', 'text': 'Text 2', 'pk': 2},
#             {'title': 'Post 3', 'text': 'Text 3', 'pk': 3},
#     ]
#     # return HttpResponse('hello world')
#     # return HttpResponse('<h1>hello world</h1>') # 태그와 결합하여 사용 가능

#     # 템플릿 태그는 아래처럼 해석되어 들어갑니다.
#     # 그렇게 때문에 css, js를 같은 폴더에서 읽어오지 못합니다.
#     # s = '<h1>{{title}}</h><p>{{text}}</p>'
#     # return HttpResponse(s.replace('{{title}}', data[0]['title']).replace("{{text}}", data[0]["text"]))

#     # header = '<h2>hello world header</h2>'
#     # main = render_to_string("blog/test.txt", {"data": data[0]}) # data[0] 객체를 보내고 data라는 변수로 사용하겠다. 그 후 string 형식으로 불러와 main 변수에 할당
#     # footer = '<h2>hello world footer</h2>'

#     # '''
#     # test.txt는 어떤 내용을 넣을 거냐면
#     # <p>hello blog</p>
#     # <p>{{data.title}}</p>
#     # <p>{{data.text}}</p>
#     # '''
#     # return HttpResponse(header + main + footer)

#     # 데이터를 받아서 뿌리는 것
#     return JsonResponse(data, safe=False)
    
#     # return render(request, "blog_test.html")


# def blog_detail(request, pk):
#     return render(request, "blog_detail.html")


# 오전 DB를 활용한 blog 예시 2
from django.shortcuts import render, redirect
from .models import Post


def blog_list(request):
    blogs = Post.objects.all()
    context = {"db": blogs}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {"db": blog}
    return render(request, "blog/blog_detail.html", context)


def blog_create(request, title): 
    # http://127.0.0.1:8000/create/orm 경로 입력 시 orm이라는 데이터를 생성하고 db에 저장한다.
    # url의 title을 통해 Post class 의 속성 값을 작성
    contents = 'hello world {title}'
    q = Post.objects.create(title=title, contents = contents) # 데이터 새로 생성
    q.save() # DB에 반영

    # 게시물을 저장 시 출력할 화면을 정의
    return redirect("blog_list") # urls.py에 blog_list라는 name을 가진 경로로 바로 접속하도록 한다(redirect)

def blog_delete(request, pk): 
    q = Post.objects.get(pk=pk) # pk 값이 매개변수의 pk인 것을 가져와 삭제한다.
    q.delete()
    return redirect("blog_list")


def blog_test(request):
    return render(request, "blog/blog_test.html")

