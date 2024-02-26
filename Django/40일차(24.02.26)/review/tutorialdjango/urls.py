from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]

# url에 media가 들어오게 된다면 setings의 media_root로 연결하겠다(해당 경로를 사용하겠다.)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)