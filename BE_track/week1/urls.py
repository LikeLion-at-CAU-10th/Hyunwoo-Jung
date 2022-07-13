
from django.contrib import admin
from django.urls import path,include
from posts.views import index,http_response,json_response
from .settings import MEDIA_URL,MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('',http_response,name='http_response'),
    path('json/',json_response,name='json_response'),
    path('todomate/',include("todomate.urls")),
    path('profiles/',include("profiles.urls")),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

