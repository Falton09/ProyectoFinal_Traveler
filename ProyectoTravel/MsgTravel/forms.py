from django import forms
from MsgTravel.models import Mensajeria


class EnvioMensaje(forms.ModelForm):

    class Meta:
        model = Mensajeria
        fields=['mensaje']
        labels= {'mensaje': (""),}


