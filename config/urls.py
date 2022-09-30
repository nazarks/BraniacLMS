from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic import RedirectView

from config import settings
from mainapp import views

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("img/favicon.ico"))),
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    path("social_auth/", include("social_django.urls", namespace="social")),
    path("mainapp/", include("mainapp.urls", namespace="mainapp")),
    path("authapp/", include("authapp.urls", namespace="authapp")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
