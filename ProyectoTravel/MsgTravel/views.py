from django.shortcuts import render,redirect
from MsgTravel.forms import EnvioMensaje,EnvioMensajeReseptor
from MsgTravel.models import Mensajeria, Hilo
from django.contrib.auth.models import User
from django.contrib import messages



def elegir_reseptor(request):
    
    user=request.user.username
    chats=Hilo.objects.filter(emisor=user)
    chats_reseptor=Hilo.objects.filter(reseptor=user)
    
    
    reseptor1=User.objects.all().exclude(username=request.user)
    
    contexto = {
        
        'reseptor':reseptor1,
        'chats':chats,
        'chats_reseptor':chats_reseptor,
        

    }
    return render(request, 'MsgTravel/elejir_reseptor.html',contexto)

def mensaje(request,username):
    user = request.user.username
    users= Hilo.objects.filter(emisor=user,reseptor=username)
    users1= Hilo.objects.filter(emisor=username,reseptor=user)
   
    if users or users1:
        messages.info(request, 'ya esta en conversacion con este Usuario')
        return redirect('MsgTravelElegirReseptor')
    else:
        user = request.user.username
        hilos= Hilo(emisor=user,reseptor=username)
        hilos.save()
        return redirect('MsgTravelElegirReseptor')

 

def en_conversacion(request,reseptor):
    user=request.user.username
    # emisor1=(Hilo.objects.all().values('emisor'))[0]
    # emisor2=(Hilo.objects.all().values('reseptor'))[0]
    emisore=Hilo.objects.filter(emisor=user,reseptor=reseptor)
    
    if emisore:
        chat = Mensajeria.objects.filter(emisor=user,reseptor=reseptor)
        orden1="text-right" 
        orden2="text-left"
    else:
        chat = Mensajeria.objects.filter(reseptor=user,emisor=reseptor)
        orden1="text-left"
        orden2="text-right"

    if request.method == 'POST':
       
        form = EnvioMensaje(request.POST)
        print(form)
        if form.is_valid() :
            data = form.cleaned_data
            user = request.user.username
            
            if emisore:
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
        'orden1':orden1,
        'orden2':orden2, 
        'usuario':reseptor,
        
        

    }
    return render(request, 'MsgTravel/chat.html',contexto)


