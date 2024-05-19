from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"mdeditor/", include("mdeditor.urls")),
    path("", include("post.urls")),
    path("", include("artgpt.urls")),
    path("", include("signin.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
