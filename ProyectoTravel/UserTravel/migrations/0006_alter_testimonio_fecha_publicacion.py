# Generated by Django 4.1 on 2022-09-23 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserTravel', '0005_alter_testimonio_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonio',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 10, 50, 52, 108477)),
        ),
    ]
