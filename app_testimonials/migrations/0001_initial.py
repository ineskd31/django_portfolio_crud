# Generated by Django 4.2.1 on 2023-06-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=100)),
                ('citation', models.TextField()),
                ('image', models.CharField(max_length=700)),
            ],
        ),
    ]