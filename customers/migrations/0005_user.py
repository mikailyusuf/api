# Generated by Django 3.0 on 2020-11-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_remove_customers_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('ifLogged', models.BooleanField(default=False)),
                ('token', models.CharField(default='', max_length=500, null=True)),
            ],
        ),
    ]
