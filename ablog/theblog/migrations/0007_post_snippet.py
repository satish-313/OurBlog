# Generated by Django 3.1.1 on 2020-09-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20200927_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click here for reading more', max_length=300),
        ),
    ]