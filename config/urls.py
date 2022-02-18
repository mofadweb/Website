from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("ckeditor/", include("ckeditor_uploader.urls")),
        path("", include("blog.urls")),
        path("", include("archives.urls")),
        path("events/", include("events.urls")),
        path("hierarchy/", include("leadership.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
