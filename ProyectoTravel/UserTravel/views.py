from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from UserTravel.forms import UserEditFrom, UserRegisterForm, AvatarForm,Testimonios,Comentario
from UserTravel.models import Avatar,Testimonio,ComentarioTestimonio



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



def subir_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            
            user = request.user
            avatar = Avatar.objects.filter(user=user)

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
    
    if request.method == 'POST':

        form = UserEditFrom(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data['username']
            usuario.email = data['email']
            usuario.save()

            
        
            return redirect('UserTravelPerfil')
    contexto = {
        'usuario':usuario,
        'form': UserEditFrom(
            initial={
                'username': usuario.username,
                'email': usuario.email,
                'usuario': usuario               
            }            
        ),
        'titulo':"TRAVELER - Editar Usuario",
        'subtitulo':"Editar Usuario",
        'boton': "Editar"
    }

    return render(request, 'UserTravel/base_plantilla.html', contexto)

#esto no funciona 
def editar_contrasena(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,
                             'Your password was successfully updated!',
                             extra_tags='alert-success')
            

            
        
            return redirect('UserTravelPerfil')
    contexto = {
        'form':PasswordChangeForm(user=request.user),
        'titulo':"TRAVELER - Editar Usuario",
        'subtitulo':"Editar Usuario",
        'boton': "Editar"
    }

    return render(request, 'UserTravel/base_plantilla.html', contexto)



def testimonio(request):
    if request.method == 'POST':
        mi_formulario = Testimonios(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            user = request.user
            

            testimonio1 = Testimonio(user=user,titulo=data.get('titulo'),texto=data.get('texto'))
            testimonio1.save()

            return redirect('UserTravelPerfil')
   
    contexto = {
        'form': Testimonios(), 
        
    }


    return render(request, 'UserTravel/crear_testimonio.html',contexto)


def ver_testimonios(request):
    user = request.user
    testimonio=Testimonio.objects.filter(user=user)

     
    contexto = {
        'testimonio':testimonio,
        
    }
    return render(request, 'UserTravel/ver_testimonios.html',contexto)




def edit_testimonio(request,id):
    edit_test=Testimonio.objects.get(id=id)

    if request.method =='POST':
        mi_formulario = Testimonios(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            edit_test.titulo = data.get('titulo')
            edit_test.texto = data.get('texto')
            edit_test.save()
            return redirect('UserTravelTestimonio')
    
    contexto = {
        'form': Testimonios(
            initial={
                'titulo': edit_test.titulo,
                'texto': edit_test.texto,
            }
        ),       
        
    }
    return render(request, 'UserTravel/crear_testimonio.html', contexto)

def eliminar_testimonio(request, id):
    eliminar_testimonio = Testimonio.objects.get(id=id)
    eliminar_testimonio.delete()

    messages.info(request, f"El Testimonio fue eliminado")

    return redirect("UserTravelTestimonio")


def chatestimonio(request,id):
    chattest=Testimonio.objects.get(id=id)
    mostrar_coment=ComentarioTestimonio.objects.filter(id_testimonio=id)

    if request.method == 'POST':
        mi_formulario = Comentario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            user = request.user
            

            comentario1 = ComentarioTestimonio(id_testimonio=chattest,user_comentario=user,comentario=data.get('comentario'))
            comentario1.save()

            return redirect('AppTravelInicio')


    contexto={
        'form':Comentario(),
        'testimonios':chattest,
        'comentario': mostrar_coment,
    }

    return render(request, 'UserTravel/chat_testimonio.html',contexto)


def ver_comentarios(request):
    user = request.user
    comentario=ComentarioTestimonio.objects.filter(user_comentario=user)

     
    contexto = {
        'comentario':comentario,
        
    }
    return render(request, 'UserTravel/ver_comentarios.html',contexto)

def edit_comentario(request,id):
    edit_comen=ComentarioTestimonio.objects.get(id=id)

    if request.method =='POST':
        mi_formulario = Comentario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            
            edit_comen.comentario = data.get('comentario')
            edit_comen.save()
            return redirect('UserTravelVerComentarios')
    
    contexto = {
        'form': Comentario(
            initial={
                'comentario': edit_comen.comentario,
            }
        ),       
        
    }
    return render(request, 'UserTravel/editar_comentario.html', contexto)


def eliminar_comentario(request,id):
    eliminar_comentario = ComentarioTestimonio.objects.get(id=id)
    eliminar_comentario.delete()

    messages.info(request, f"El Comentario fue eliminado")

    return redirect("UserTravelVerComentarios")