import json
from datetime import datetime

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from wagyuer.models import WagyuInfomation, WagyuPackageImg
from wagyuer.modules.wagyuer import Wagyuer

from .serializers import PackageSerializer


class PackageViewSet(ModelViewSet):
    queryset = WagyuPackageImg.objects.all()  # ここが対象となるレコードの指定．今回は全部
    serializer_class = PackageSerializer  # 戻り値を定義したSerializer

    def create(self, request, *args, **kwargs):
        # response = super().create(request, *args, **kwargs)

        # # get wagyu infomation
        # img_path = WagyuPackageImg.objects.latest("upload_date").img.path
        # wagyuer = Wagyuer(img_path)
        # wagyu_infomation = wagyuer.main()

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

        # serialize model object to json
        # wagyu_info = WagyuInfomation.objects.filter(id=wagyu_info.pk)
        wagyu_info = WagyuInfomation.objects.filter(id=40)
        wagyu_info_json = serializers.serialize("json", wagyu_info)

        return Response(wagyu_info_json)


        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
