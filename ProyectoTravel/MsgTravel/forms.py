from django import forms
from django.contrib.auth.models import User

from MsgTravel.models import Mensajeria


class EnvioMensaje(forms.ModelForm):

    class Meta:
        model = Mensajeria
        fields=['mensaje']
