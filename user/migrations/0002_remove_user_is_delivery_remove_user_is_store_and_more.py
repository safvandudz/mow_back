# Generated by Django 4.2.5 on 2023-09-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_delivery',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_store',
        ),
        migrations.AddField(
            model_name='user',
            name='is_restuarant',
            field=models.BooleanField(default=False, verbose_name='Is restuarant'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user_user',
        ),
    ]
