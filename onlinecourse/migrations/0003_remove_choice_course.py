# Generated by Django 3.1.3 on 2023-02-27 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230227_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='course',
        ),
    ]