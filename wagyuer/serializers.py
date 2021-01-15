from rest_framework import serializers

from .models import WagyuPackageImg


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WagyuPackageImg
        fields = ("img",)
