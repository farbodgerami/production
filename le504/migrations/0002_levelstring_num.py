# Generated by Django 3.2.9 on 2022-07-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('le504', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelstring',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
