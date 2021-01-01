from django.db import models


class WagyuPackageImg(models.Model):
    """和牛パッケージ写真(実際にはパス）を保存するテーブル"""

    img = models.ImageField(verbose_name="アップロード画像")


class WagyuInfomation(models.Model):
    """個体識別番号で検索した和牛の情報を、記録するテーブル"""

    wagyu_recognition_id = models.CharField(verbose_name="個体識別番号", max_length=255)
    date_of_birth = models.DateField(verbose_name="生年月日")
    sex = models.CharField(verbose_name="性別", max_length=255)
    kind = models.CharField(verbose_name="種別", max_length=255)
    date_of_dead = models.DateField(verbose_name="と畜日")
