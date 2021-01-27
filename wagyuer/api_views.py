from datetime import datetime

from rest_framework import views
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from wagyuer.models import WagyuInfomation, WagyuPackageImg
from wagyuer.modules.wagyuer import Wagyuer

from .serializers import PackageSerializer, WagyuIdSerializer


class PackageViewSet(ModelViewSet):
    queryset = WagyuPackageImg.objects.all()  # ここが対象となるレコードの指定．今回は全部
    serializer_class = PackageSerializer  # 戻り値を定義したSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # get wagyu infomation
        img_path = WagyuPackageImg.objects.latest("upload_date").img.path
        wagyuer = Wagyuer()
        wagyu_id = wagyuer.get_individual_id(img_path)

        response.data["wagyu_id"] = wagyu_id
        return response


class WagyuInfomationAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = WagyuIdSerializer(data=request.data)
        serializer.is_valid()
        wagyu_id = serializer.validated_data["wagyu_id"]
        wagyuer = Wagyuer()
        wagyu_infomation = wagyuer.get_wagyu_infomation(wagyu_id)

        # save wagyu infomation
        wagyu_infomation_object = WagyuInfomation.objects.create(
            wagyu_package=WagyuPackageImg.objects.latest("upload_date"),
            individual_id=wagyu_infomation["個体識別番号"],
            kind=wagyu_infomation["種別"],
            sex=wagyu_infomation["性別"],
            birth_date=datetime.strptime(wagyu_infomation["出生日"], "%Y.%m.%d"),
            birth_place=wagyu_infomation["出生場所"],
            slaughter_date=datetime.strptime(wagyu_infomation["と畜日"], "%Y.%m.%d"),
            slaughter_place=wagyu_infomation["と畜場所"],
        )

        wagyu_infomation_object.save()

        return Response(wagyu_infomation)
