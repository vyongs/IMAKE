# Generated by Django 3.0.6 on 2020-05-27 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20200527_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='contents',
        ),
    ]
