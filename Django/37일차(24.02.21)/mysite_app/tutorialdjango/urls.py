from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls')), # 해당 URL로 들어오면 main앱에 urls.py를 참고하겠다! => main > urls.py로 연결하는 것! 
    # path("about/", include('main.urls')), # 로컬주소/about 의 경로도 main에서 처리.
    # about/의 경로는 로컬 호스트/""/about 인것 


    path("blog/", include('blog.urls')), # 해당 url로 들어오면 blog앱의 urls.py롤 사용하겠다.
    # path("blog/<int:pk>/", blogdetails), # 이것은 여기서 처리하지 않고 blog앱에 urls.py에서 처리하면 됩니다! => 즉 blog/ 처럼 blog후 / 되어 경로를 사용하는 것들은 전부 blog > urls.py에서 처리한다.
    # path("blog/1", blog1) # 기존에는 이렇게 처리했는데
    # path("blog/1", blog2) # include()를 통해 해당 앱에서 처리하도록 해당 경로를 해당 앱의 urls.py을 연결
    # path("blog/1", blog3) # 이런 경로들의 내용들은 blog > urls.py에서 처리하는것(include로 blog 경로로 들어오는 것들은 blog의 urls.py에서 처리하도록 설정함)

    # accouts/ 로 들어온 경로들 모두를 accounts > urls.py에서 처리되도록 전달
    path("accounts/", include('accounts.urls')),
]