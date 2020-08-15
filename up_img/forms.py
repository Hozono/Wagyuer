from django import forms

from .models import WagyuPackageImg


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = WagyuPackageImg
        fields = "__all__"
