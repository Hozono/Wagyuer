from datetime import datetime

from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from wagyuer.forms import ImageUploadForm
from wagyuer.models import WagyuPackageImg, WagyuInfomation
from wagyuer.modules.wagyuer import Wagyuer


class IndexView(CreateView):

    model = WagyuPackageImg
    form_class = ImageUploadForm
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        # get wagyu infomation
        img_path = WagyuPackageImg.objects.latest("upload_date").img.path
        wagyuer = Wagyuer(img_path)
        wagyu_infomation = wagyuer.main()

        # save wagyu infomation
        WagyuInfomation.objects.create(
            wagyu_package=WagyuPackageImg.objects.latest("upload_date"),
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

    def get_success_url(self):
        pk = WagyuInfomation.objects.latest("insert_date").pk
        return reverse_lazy("wagyuer:wagyu_infomation", kwargs={"pk": pk})


class WagyuInfomationView(DetailView):
    model = WagyuInfomation
    template_name = "wagyu_infomation.html"
    context_object_name = "wagyu_infomation"
