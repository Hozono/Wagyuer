from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_template, name="index"),
    path("wagyu_info/", views.show_wagyu_info, name="show_wagyu_info"),
]
