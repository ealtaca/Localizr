# Generated by Django 2.0.1 on 2018-05-23 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Localizr', '0010_auto_20180523_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='user',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
