from rest_framework import serializers

from .models import WagyuPackageImg
from .modules.wagyuer import Wagyuer


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WagyuPackageImg
        fields = ("img",)


class WagyuIdSerializer(serializers.Serializer):
    wagyu_id = serializers.CharField(required=True, max_length=10, min_length=10)
