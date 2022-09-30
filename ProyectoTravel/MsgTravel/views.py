from django.shortcuts import render,redirect
from MsgTravel.forms import EnvioMensaje,EnvioMensajeReseptor
from MsgTravel.models import Mensajeria, Hilo
from django.contrib.auth.models import User
from django.contrib import messages



def elegir_reseptor(request):
    
    user=request.user.username
    chats=Hilo.objects.filter(emisor=user)
    
    
    reseptor1=User.objects.all().exclude(username=request.user)
    
    contexto = {
        
        'reseptor':reseptor1,
        'chats':chats,
        

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
            try:
                user = request.user.username
                hilos= Hilo(emisor=user,reseptor=username)
                hilos.save()
            except:
                messages.info(request, 'Usted ya esta en conversacion con este Usuario')

            return redirect('MsgTravelElegirReseptor')

    contexto = {
        'form':EnvioMensaje(),
        'usuario':username

    }
    return render(request, 'MsgTravel/enviar_mensaje.html',contexto)

def en_conversacion(request,reseptor):
    user=request.user.username
    emisor1=(Hilo.objects.all().values('emisor'))[0]
    
    if user in emisor1.values():
        chat = Mensajeria.objects.filter(emisor=user,reseptor=reseptor) 
    else:
        chat = Mensajeria.objects.filter(reseptor=user,emisor=reseptor)
   

    if request.method == 'POST':
       
        form = EnvioMensaje(request.POST)
        print(form)
        if form.is_valid() :
            data = form.cleaned_data
            user = request.user.username
            if (user in emisor1.values()):
                mensaje=Mensajeria(emisor=user,reseptor=reseptor,mensaje=data.get('mensaje'))
                mensaje.save()
                messages.info(request, 'Mensaje Enviado')
                return redirect('MsgTravelElegirReseptor')
                

            else:
                mensaje= Mensajeria(emisor=reseptor,reseptor=user,mensaje_reseptor=data.get('mensaje'))
                mensaje.save()
                messages.info(request, 'Mensaje Enviado')
                return redirect('MsgTravelElegirReseptor')
                


    contexto = {
        'form':EnvioMensaje(),
        'chat':chat,
 
        'usuario':reseptor,
        
        

    }
    return render(request, 'MsgTravel/chat.html',contexto)


