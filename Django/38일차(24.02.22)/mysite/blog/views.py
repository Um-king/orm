from django.shortcuts import render

blog_database = [
    {
        "id": 1,
        "title": "제목1",
        "content": "내용1",
        "created_at": "2021-02-22",
        "updated_at": "2021-02-22",
        "author": "홍길동",
        "category": "일상",
        "tag": ["태그1", "태그2"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 3,
        "like_user": [10, 20, 21],
    },
    {
        "id": 2,
        "title": "제목2",
        "content": "내용2",
        "created_at": "2021-02-23",
        "updated_at": "2021-02-23",
        "author": "김철수",
        "category": "일기",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 10,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 3,
        "title": "제목3",
        "content": "내용3",
        "created_at": "2021-02-24",
        "updated_at": "2021-02-24",
        "author": "이영희",
        "category": "맛집",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 20,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 4,
        "title": "제목4",
        "content": "내용4",
        "created_at": "2021-02-25",
        "updated_at": "2021-02-25",
        "author": "박민수",
        "category": "여행",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 30,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
]


def blog_list(request):
    # blogs = Blog.objects.all() # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"blog_list": blog_database}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk) # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"blog": blog_database[pk - 1]}
    return render(request, "blog/blog_detail.html", context)


# render(request, html파일, context(고정, 딕셔너리 형태))
# => html파일을 일반 텍스트로 가져옵니다. 중괄호와 같은 문법이 나오면 context에 있는 값을 가져와서 넣어줍니다. 그리고 이것을 사용자에게 넘겨주는 역활을 합니다. 넘겨줄 때에는 HttpResponse를 사용합니다.
# => request는 사용자가 보내는 요청에 대한 정보가 담겨있습니다. 이 요청에 로그인 정보 등이 담겨있습니다. 나중에는 이것을 이용해서 template에서 로그인 정보를 출력하게 한다던지, 로그인 정보가 없으면 로그인 페이지로 이동하게 한다던지 등에 기능을 할 수 있습니다.
# 함수 각각을 직접 다 읽어보시는 것은 권하지는 않습니다. 가볍게 훑어보시는 정도는 괜찮습니다. https://github.com/django/django/blob/main/django/http/response.py 여기에 있는 HttpResponse를 보시면 됩니다. 이것은 django의 공식 소스코드입니다.