# 크롤링을 위한 코드 작성 # 가상환경이기 때문에 설치
import requests 
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse


blog_list = [ # 나중에는 DB의 내용을 불러와서 담는 리스트로 만들면 됨
    {
        "id": 1,
        "title": "장고는 너무 재미있어!!!",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "파이썬도 너무 재미있어!!!!",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "자바스크립트는 별로였어!!!",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]

user_list = [
    {
        "id": 1,
        "username": "hojun",
        "email": "hojun@gmail.com",
        "password": "1234",
    },
    {
        "id": 2,
        "username": "jihun",
        "email": "jihun@gmail.com",
        "password": "1234",
    },
    {
        "id": 3,
        "username": "junho",
        "email": "junho@gmail.com",
        "password": "1234",
    },
]

# s = f'hello world' # 개행이 안되고
# ss = f'''hello world''' #개행이 됩니다.

# # 테스트용 코드 작성
# def index(request):
#     return HttpResponse("<h1>환영합니다. index 페이지입니다.</h1>")

# # 게시물 목록을 보여주는 페이지
# def bloglist(request): 
#     # 게시물 목록이 1~2개가 아닌 몇 백개의 경우 1,2,3,...100까지 작성할 수 없음
#     # 따라서 return전에 반복문을 통해 게시물에 대한 내용을 가공해주고 html문법에 포함

#     blogitem = ""
#     for i in blog_list: # 화면에 출력할 내용을 작성한다.
#         blogitem += f'<li><a href="/blog/{i["id"]}">{i["title"]}</a></li>'
#     return HttpResponse(
#         f"""
#     <h1>블로그 리스트</h1>
#     <ul>
#         {blogitem}
#     </ul>
# """)

#### 동적으로 페이지를 생성하는 작업
# def blogdetails(request, pk):
#     # 동적으로 페이지를 생성한다. 
#     # 블로그 게시물은 수천개가 존재하는데 하나씩 만들어줄 수 없음. 따라서 pk 매개변수를 통해 하나의 함수에서  pk 값에 해당하는 내용을 호출하면 됨
    
#      blog = blog_list[pk - 1]
#      return HttpResponse(
#          f"""
#      <h1>{blog['title']}</h1>
#      <p>{blog['author']}</p>
#      <p>{blog['content']}</p>
# """
#     )



# def userdetails(request, user):
#     # 접속 경로는 하나의 함수로 동작하지만 그 세부 내용은 해당 값에 대한 내용에 맞게 출력한다.
#     # 접속은 user로 접속하고 /뒤의 내용에 따라 뒤의 내용에 해당하는 페이지를 출력

#     finduser = None
#     for i in user_list:
#         if i["username"] == user:
#             finduser = i
#     if finduser is None:
#         return HttpResponse("해당 유저가 없습니다.")
#     return HttpResponse(
#         f"""
#     <h1>{finduser['username']} 님의 정보</h1>
#     <p>이름: {finduser['username']}</p>
#     <p>이메일: {finduser['email']}</p>
# """
#     )

# 실제 배포 시 render를 사용
def index(request):
    return render(request, "main/index.html")


def bloglist(request):
    # blogitem = ""
    # for i in blog_list:
    #     blogitem += f'<li><a href="/blog/{i["id"]}">{i["title"]}</a></li>'

    # blogitems이라는 이름으로 blog_list를 호출 할 수 있다!!!!!
    # blogitems를 호출하는 곳이 있다면 blog_list객체를 사용하는 것!
    context = {"blogitems": blog_list} # blogitems를 사용하는 곳에 blog_list를 전달 => templates > main > bloglist.html에서 for문에 blogitems를 사용하고 blogitems는 blog_list을 호출하는 것

    # context = {"blogitems": blogitems} # 앞의 blogitems이름으로 뒤의 blogitem 객체를 사용할 수 있도록 설정한 것
    # context = {"blogitem": blogitem, "useritem": useritem} # 여러개 작성 가능 -> useritem을 호출하는 html이 있다면 useritem의 객체 값을 사용할 수 있다.

    # 해당 html 파일로 context의 내용을 인자로 전달함
    # 해당 html에서 전달된 객체들의 내용을 사용할 수 있다. => blogitems이름으로 blog_list 사용
    return render(request, "main/bloglist.html", context) # context와 같이 "딕셔너리 형태"로 넣는 것을 템플릿 문법


def blogdetails(request, pk):
    blog = blog_list[pk - 1]
    language = ["html", "css", "js", "python"]
    context = {"blog": blog, "language": language}
    return render(request, "main/blogdetails.html", context)


def userdetails(request, user):
    finduser = None
    for i in user_list:
        if i["username"] == user:
            finduser = i
    if finduser is None:
        return render(request, "main/notfound.html")
    return render(request, "main/userdetails.html", {"user": finduser})


def bookinfo(request):
    # 해당 사이트를 크롤링한다.

    url = "https://paullab.co.kr/bookservice/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    titles = soup.select("h2")
    bookcover = soup.select(".book_cover")

    result = []

    for title, cover in zip(titles, bookcover):
        result.append((title.text, "https://paullab.co.kr/bookservice/" + cover["src"]))

    return render(request, "main/bookinfo.html", {"bookinfo": result})

