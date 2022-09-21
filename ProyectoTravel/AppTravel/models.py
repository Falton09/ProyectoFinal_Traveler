from django.db import models

from django.contrib.auth.models import User


class NombreDestino(models.Model):
    destino=models.CharField(max_length=40)

    def __str__(self):
        return f"Pais: {self.destino}"

class Vuelo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    destino = models.ForeignKey(NombreDestino, on_delete=models.CASCADE, null=True)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    num_personas = models.IntegerField()
    def __str__(self):
        return f"{self.destino}"


class NombreHotel(models.Model):
    destino = models.ForeignKey(NombreDestino, on_delete=models.CASCADE,null=True)
    nombreh = models.CharField(max_length=40)

    def __str__(self):
       return f"{self.nombreh}({self.destino})"


class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nombreH = models.ForeignKey(NombreHotel, on_delete=models.CASCADE,null=False, blank=False)
    num_personas = models.IntegerField()
    dia_entrada = models.DateField()
    dia_salida = models.DateField()
    def __str__(self):
       return f"{self.nombreH}"

