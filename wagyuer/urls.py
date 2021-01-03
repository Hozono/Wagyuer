from django.urls import path
from .views import IndexView, WagyuInfomationView

app_name = "wagyuer"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "wagyu_infomation/<int:pk>",
        WagyuInfomationView.as_view(),
        name="wagyu_infomation",
    ),
]
