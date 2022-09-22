from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from UserTravel.forms import UserRegisterForm, AvatarForm
from UserTravel.models import Avatar



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de Sesion Satisfactorio!')

            else:
                messages.info(request, 'Porfavor Verificar Usuario o Contrasenia!')
        else:
            messages.info(request, 'Inicio de Sesion Fallido!')

        return redirect('AppTravelInicio')

    contexto = {
        'form': AuthenticationForm(),
        'titulo':"TRAVELER - Login",
        'subtitulo':"Inicio de Sesion",
        'boton': "Loguearse"

    }
    return render(request, 'UserTravel/base_plantilla.html', contexto)

def registro(request):

    if request.method == 'POST':

        
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu Usuario fue Registrado Satisfactoriamente!')
        else:
            messages.info(request, 'Tu Usuario no pudo ser Registrado!')
        return redirect('AppTravelInicio')

    contexto = {
        
        'form': UserRegisterForm(),
        'titulo':"TRAVELER - Registro",
        'subtitulo':"Registro de Usuario",
        'boton': "Crear Usuario"
    }

    return render(request, 'UserTravel/base_plantilla.html', contexto)



def subir_avatar(request):# parece todo en regal, pero no me muestra la foto en la pagina
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))
            user = request.user

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=user, imagen=data.get("imagen"))
                avatar.save()

        return redirect("AppTravelInicio")

    contexto = {
        "form": AvatarForm(),
        'titulo':"TRAVELER - Avatar",
        'subtitulo':"Agregar Avatar",
        'boton': "Crear"
        
        
    }
    return render(request, "UserTravel/base_plantilla.html", contexto)

def perfil(request):

    return render(request, "UserTravel/perfil.html")

def editar_usuario(request):
    usuario = request.user
    email=request.user.email
    if request.method == 'POST':

       
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            email = data.get('email')
            usuario.password1 = data.get('password1')
            usuario.password2 = data.get('password2')
            usuario.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('AppTravelInicio')
    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(
            initial={
                'username': usuario.username,
                'email': email,
                
            }),
        'titulo':"TRAVELER - Editar",
        'subtitulo':"Editar Usuario",
        'boton': "Editar"
    }

    return render(request, 'UserTravel/base_plantilla.html', contexto)
