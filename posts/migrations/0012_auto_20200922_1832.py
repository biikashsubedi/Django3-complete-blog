# Generated by Django 3.1.1 on 2020-09-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200922_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
