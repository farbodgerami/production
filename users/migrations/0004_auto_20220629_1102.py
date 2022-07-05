# Generated by Django 3.2.9 on 2022-06-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='paidnuntil',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userplan',
            field=models.CharField(default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phonenumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
