# Generated by Django 3.0.6 on 2020-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_remove_article_contents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usetime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
