from django.db import models


class WagyuPackageImg(models.Model):
    """和牛パッケージ写真を保存するモデル"""

    upload_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(verbose_name="アップロード画像", upload_to="uploads/%Y/%m/%d/")


class WagyuInfomation(models.Model):
    """和牛情報を保存するテーブル"""

    wagyu_package = models.ForeignKey(to=WagyuPackageImg, on_delete=models.CASCADE)
    insert_date = models.DateTimeField(auto_now_add=True)
    individual_id = models.CharField(
        verbose_name="個体識別番号", blank=True, null=True, max_length=255
    )
    kind = models.CharField(verbose_name="種別", blank=True, null=True, max_length=255)
    sex = models.CharField(verbose_name="性別", blank=True, null=True, max_length=255)
    birth_date = models.DateField(verbose_name="出生日", blank=True, null=True)
    birth_place = models.CharField(
        verbose_name="出生場所", blank=True, null=True, max_length=255
    )
    slaughter_date = models.DateField(verbose_name="と畜日", blank=True, null=True)
    slaughter_place = models.CharField(
        verbose_name="と畜場所", blank=True, null=True, max_length=255
    )
