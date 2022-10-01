from enum import unique
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Mensajeria(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    emisor = models.CharField(max_length=30)
    reseptor = models.CharField(max_length=30)
    mensaje= RichTextField()
    mensaje_reseptor = RichTextField(blank=True)
    fecha_creacion_mensaje = models.DateTimeField(auto_now_add=True)

class Hilo(models.Model):
    emisor= models.CharField(max_length=50,)
    reseptor= models.CharField(max_length=50, )
    def __str__(self):
        return f"emisor:{self.emisor},reseptor:{self.reseptor}"