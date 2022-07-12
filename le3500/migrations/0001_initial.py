# Generated by Django 3.2.9 on 2022-07-08 15:05

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import le3500.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kalame', models.CharField(max_length=300, null=True)),
                ('maani', models.CharField(blank=True, max_length=300, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('lesson', models.IntegerField(default=1)),
                ('audiofile', models.FileField(blank=True, null=True, upload_to='3500audio/', validators=[le3500.models.validatefileextension])),
            ],
        ),
        migrations.CreateModel(
            name='Levelstring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.TextField(default='{}')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelstring3', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
