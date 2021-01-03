from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("", include("wagyuer.urls")),
]
