from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default="default.png",upload_to='avatares', null=False)

    def __str__(self):
       return f"{self.user}"

class Testimonio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50, null=True)
    texto = RichTextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return f"Titulo:{self.titulo},Usuario:{self.user}"


class ComentarioTestimonio(models.Model):
    id_testimonio = models.ForeignKey(Testimonio, on_delete=models.CASCADE, null=True)
    user_comentario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comentario= RichTextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

