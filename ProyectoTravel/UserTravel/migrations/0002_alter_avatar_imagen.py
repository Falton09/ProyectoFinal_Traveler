# Generated by Django 4.1 on 2022-09-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserTravel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to='avatares'),
        ),
    ]
