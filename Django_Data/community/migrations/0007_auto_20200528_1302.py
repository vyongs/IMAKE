# Generated by Django 3.0.6 on 2020-05-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20200528_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user_info',
            field=models.CharField(default='no-user', max_length=100),
        ),
    ]