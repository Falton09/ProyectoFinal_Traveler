# Generated by Django 4.1 on 2022-09-30 11:46

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MsgTravel', '0008_alter_mensajeria_fecha_creacion_mensaje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajeria',
            name='fecha_creacion_mensaje',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 8, 46, 15, 740678)),
        ),
        migrations.AlterField(
            model_name='mensajeria',
            name='mensaje_reseptor',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
