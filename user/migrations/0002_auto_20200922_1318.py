# Generated by Django 2.0 on 2020-09-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=20, verbose_name='昵称'),
        ),
    ]
