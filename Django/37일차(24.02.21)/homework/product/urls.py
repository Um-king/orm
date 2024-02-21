from django.urls import path
from .views  import product, productdetails

urlpatterns = [
    # blog/ 가 없이 ""만 사용 -> 이미 앞에 튜토리얼장고 urls.py에서 blog/한 경로를 연결했기 때문에 여기서는 blog/ 이후의 경로가 작성되어야한다.
    # blog/경로 이렇게 하면 x
    # 이미 blog경로로 들어왔을때 여기로 연결되었기 때문에 그 이후의 경로를 작성한다. (blog/ 작성 x)
    path("", product), 
    path("<int:pk>/", productdetails),
]
