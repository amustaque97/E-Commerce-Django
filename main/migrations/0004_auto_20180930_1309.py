# Generated by Django 2.1.1 on 2018-09-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180922_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
