from django.shortcuts import render,redirect
from MsgTravel.forms import EnvioMensaje
from MsgTravel.models import Mensajeria
from django.contrib.auth.models import User

def elegir_reseptor(request):
    reseptor=User.objects.all()

    contexto = {
        'reseptor':reseptor

    }
    return render(request, 'MsgTravel/elejir_reseptor.html',contexto)

def mensaje(request,username):
    if request.method == 'POST':
        form = EnvioMensaje(request.POST)

        if form.is_valid() :
            data = form.cleaned_data
            user = request.user

            mensaje= Mensajeria(emisor=user,reseptor=username,mensaje=data.get('mensaje'))
            mensaje.save()

            return redirect('AppTravelInicio')

    contexto = {
        'form':EnvioMensaje()

    }
    return render(request, 'MsgTravel/enviar_mensaje.html',contexto)