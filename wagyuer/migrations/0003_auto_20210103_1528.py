# Generated by Django 3.1.4 on 2021-01-03 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagyuer', '0002_auto_20210103_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wagyupackageimg',
            old_name='upload_data',
            new_name='upload_date',
        ),
    ]
