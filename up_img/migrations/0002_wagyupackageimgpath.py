# Generated by Django 2.2.12 on 2020-08-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('up_img', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WagyuPackageImgPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.ImageField(upload_to='', verbose_name='アップロード画像')),
            ],
        ),
    ]
