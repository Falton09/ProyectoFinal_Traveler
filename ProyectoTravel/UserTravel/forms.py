from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from UserTravel.models import Avatar


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

class Testimonios(forms.Form):
    texto = forms.CharField(max_length=50,widget=forms.Textarea)


class UserEditFrom(UserCreationForm):

    username = forms.CharField(label="Modificar Nombre")
    email= forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ['username','email', 'password1','password2']
        help_texts = {k:"" for k in fields}