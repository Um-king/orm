from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

# MEDIA URL을 MEDIA ROOT로 처리하겠다.
# settings.MEDIA_URL 해당 url로 접속하면 document_root=settings.MEDIA_ROOT로 처리하겠다. 
# 우리가 settings.py 설정한 미디어 경로로 처리하겠다
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)