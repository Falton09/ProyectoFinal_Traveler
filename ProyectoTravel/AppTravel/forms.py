from datetime import datetime
from django import forms
from AppTravel.models import Hotel, NombreDestino, NombreHotel, Vuelo



class NuevoVuelo(forms.Form):
    
    destino = forms.ModelChoiceField(queryset=NombreDestino.objects.all())
    fecha_salida = forms.DateField( initial=datetime.now(),input_formats=['%d-%m-%Y'],widget=forms.DateInput(format = '%d-%m-%Y'))
    fecha_regreso = forms.DateField(initial=datetime.now(),input_formats=['%d-%m-%Y'],widget=forms.DateInput(format = '%d-%m-%Y'))
    num_personas = forms.IntegerField()

class ReservaHotel(forms.Form):
    nombreH = forms.ModelChoiceField(queryset=NombreHotel.objects.all(),widget=forms.Select(attrs={'class': 'col-md-auto'}))
    num_personas = forms.IntegerField()
    dia_entrada = forms.DateField(initial=datetime.now(),input_formats=['%d-%m-%Y'],widget=forms.DateInput(format = '%d-%m-%Y') )
    dia_salida = forms.DateField(initial=datetime.now(),input_formats=['%d-%m-%Y'],widget=forms.DateInput(format = '%d-%m-%Y'))
    def __str__(self):
       return f"{self.nombreh}({self.destino})"


class BusquedaVuelos(forms.Form):
    destino = forms.ModelChoiceField(queryset=Vuelo.objects.all(),label=("Vuelos"))

class BusquedaResevas(forms.Form):
    nombreH = forms.ModelChoiceField(queryset=Hotel.objects.all(),label=("Hoteles"))

