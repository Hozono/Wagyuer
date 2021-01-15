from rest_framework.viewsets import ModelViewSet

from .models import WagyuPackageImg
from .serializers import PackageSerializer


class PackageViewSet(ModelViewSet):
    queryset = WagyuPackageImg.objects.all()  # ここが対象となるレコードの指定．今回は全部
    serializer_class = PackageSerializer  # 戻り値を定義したSerializer
