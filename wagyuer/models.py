from django.db import models


class WagyuPackageImg(models.Model):
    """和牛パッケージ写真(実際にはパス）を保存するテーブル"""

    upload_date = models.DateField(auto_now_add=True)
    img = models.ImageField(verbose_name="アップロード画像")
