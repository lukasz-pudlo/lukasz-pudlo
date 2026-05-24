from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include
from django.urls import path

urlpatterns = [
    path("healthz/", lambda request: HttpResponse("ok"), name="healthz"),
    path("admin/", admin.site.urls),
    path("", include("lukasz_pudlo.pages.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
