from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from UserTravel.models import Avatar, Testimonio,ComentarioTestimonio


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class Testimonios(forms.ModelForm):
    
    class Meta:
        model = Testimonio
        fields=['titulo','texto']

class Comentario(forms.ModelForm):
    
    class Meta:
        model = ComentarioTestimonio
        fields=['comentario']




class UserEditFrom(forms.Form):

    username = forms.CharField(label="Modificar Nombre")
    email= forms.EmailField(label="Modificar E-mail")

#class PasswordChangeForm(forms.ModelForm):

    