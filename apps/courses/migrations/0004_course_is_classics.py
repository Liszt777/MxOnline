# Generated by Django 2.2 on 2019-09-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_classics',
            field=models.BooleanField(default=False, verbose_name='是否为经典课程'),
        ),
    ]
