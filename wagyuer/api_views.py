import json
from datetime import datetime

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import generics, views
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
        individual_num = wagyuer.get_individual_id(img_path)

        # # save wagyu infomation
        # wagyu_info = WagyuInfomation.objects.create(
        #     wagyu_package=WagyuPackageImg.objects.latest("upload_date"),
        #     individual_id=wagyu_infomation["individual_id"],
        #     kind=wagyu_infomation["kind"],
        #     sex=wagyu_infomation["sex"],
        #     birth_date=datetime.strptime(wagyu_infomation["birth_date"], "%Y.%m.%d"),
        #     birth_place=wagyu_infomation["birth_place"],
        #     slaughter_date=datetime.strptime(
        #         wagyu_infomation["slaughter_date"], "%Y.%m.%d"
        #     ),
        #     slaughter_place=wagyu_infomation["slaughter_place"],
        # )

        # wagyu_info.save()

        # # serialize model object to json
        # wagyu_info = WagyuInfomation.objects.filter(id=wagyu_info.pk)
        # wagyu_info_json = serializers.serialize("json", wagyu_info)

        # return response(wagyu_info_json)

        # return Response(wagyu_info_json)
        response.data["individual_num"] = individual_num
        return response


class WagyuInfomationAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = WagyuIdSerializer(data=request.data)
        serializer.is_valid()
        wagyu_id = serializer.validated_data["wagyu_id"]
        wagyuer = Wagyuer()
        wagyu_infomation = wagyuer.get_wagyu_infomation(wagyu_id)

        return Response(wagyu_infomation)
