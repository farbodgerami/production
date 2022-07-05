# Generated by Django 3.2.9 on 2022-06-29 05:48

from django.db import migrations, models
import le504.models


class Migration(migrations.Migration):

    dependencies = [
        ('le504', '0003_delete_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='audiofile',
            field=models.FileField(blank=True, null=True, upload_to='504audio/', validators=[le504.models.validatefileextension]),
        ),
    ]
