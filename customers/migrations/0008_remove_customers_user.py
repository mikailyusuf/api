# Generated by Django 3.0 on 2020-11-17 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20201117_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='user',
        ),
    ]