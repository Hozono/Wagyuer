from django.urls import include, path

from .api_urls import package_router
from .views import IndexView, WagyuInfomationView

app_name = "wagyuer"

api_urlpatterns = [  # apiのURL一覧
    path("packages/", include(package_router.urls)),  # 慣例として複数形にする
]

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "wagyu_infomation/<int:pk>",
        WagyuInfomationView.as_view(),
        name="wagyu_infomation",
    ),
    path(
        "api/0.1/",
        include(api_urlpatterns),
        name="api_package",
    ),
]
