from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_ts
from apps.middleware_mode import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/v1/", include("api.router")),
    path("", views.index, name='index'),
]
urlpatterns += doc_ts

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
