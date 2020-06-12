from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_template, name="index_template"),
]
