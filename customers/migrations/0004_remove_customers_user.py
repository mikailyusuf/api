# Generated by Django 3.0 on 2020-11-16 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customers_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='user',
        ),
    ]