# Generated by Django 4.2.1 on 2023-06-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
