# Generated by Django 4.1 on 2022-09-30 11:45

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MsgTravel', '0007_alter_mensajeria_fecha_creacion_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajeria',
            name='fecha_creacion_mensaje',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 8, 45, 42, 744735)),
        ),
        migrations.AlterField(
            model_name='mensajeria',
            name='mensaje_reseptor',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
