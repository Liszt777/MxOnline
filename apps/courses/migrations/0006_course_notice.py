# Generated by Django 2.2 on 2019-09-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_coursetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='notice',
            field=models.CharField(default='暂无公告', max_length=300, verbose_name='课程公告'),
        ),
    ]
