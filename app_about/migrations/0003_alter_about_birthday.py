# Generated by Django 4.2.1 on 2023-06-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_about', '0002_alter_about_birthday_alter_about_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='birthday',
            field=models.CharField(max_length=30),
        ),
    ]