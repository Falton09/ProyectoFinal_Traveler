from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Mensajeria(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    emisor = models.CharField(max_length=30)
    reseptor = models.CharField(max_length=30)
    mensaje = RichTextField()
    fecha_creacion_mensaje = models.DateTimeField(default=datetime.now())