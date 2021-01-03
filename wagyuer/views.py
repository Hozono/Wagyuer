from django.views.generic import CreateView
from django.urls import reverse_lazy

from wagyuer.forms import ImageUploadForm
from wagyuer.models import WagyuPackageImg
from wagyuer.modules.wagyuer import Wagyuer


class Index(CreateView):

    model = WagyuPackageImg
    form_class = ImageUploadForm
    template_name = "index.html"
    success_url = reverse_lazy("wagyuer:index")

    def post(self, request, *args, **kwargs):
        wagyuer = Wagyuer()
        return super().post(request, *args, **kwargs)

