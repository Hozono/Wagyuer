from datetime import datetime

from django.views.generic import CreateView
from django.urls import reverse_lazy

from wagyuer.forms import ImageUploadForm
from wagyuer.models import WagyuPackageImg, WagyuInfomation
from wagyuer.modules.wagyuer import Wagyuer


class Index(CreateView):

    model = WagyuPackageImg
    form_class = ImageUploadForm
    template_name = "index.html"
    success_url = reverse_lazy("wagyuer:index")

    def post(self, request, *args, **kwargs):
        wagyu_package = WagyuPackageImg.objects.latest("upload_date")
        img_path = WagyuPackageImg.objects.latest("upload_date").img.path
        wagyuer = Wagyuer(img_path)
        wagyu_infomation = wagyuer.main()
        WagyuInfomation.objects.create(
            wagyu_package=wagyu_package,
            individual_id=wagyu_infomation["individual_id"],
            kind=wagyu_infomation["kind"],
            sex=wagyu_infomation["sex"],
            birth_date=datetime.strptime(wagyu_infomation["birth_date"], "%Y.%m.%d"),
            birth_place=wagyu_infomation["birth_place"],
            slaughter_date=datetime.strptime(
                wagyu_infomation["slaughter_date"], "%Y.%m.%d"
            ),
            slaughter_place=wagyu_infomation["slaughter_place"],
        )
        return super().post(request, *args, **kwargs)
