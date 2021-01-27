from django.contrib import admin

from wagyuer.models import WagyuPackageImg, WagyuInfomation

admin.site.register(WagyuPackageImg)


class WagyuInfomationAdmin(admin.ModelAdmin):
    list_display = ("pk",)


admin.site.register(WagyuInfomation, WagyuInfomationAdmin)
