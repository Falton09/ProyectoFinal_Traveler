from django.contrib.auth.views import LogoutView
from django.urls import path

from UserTravel.views import *

urlpatterns = [
    path('login/', login_request, name='UserTravelLogin'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='UserTravelLogout'),
    path('registro/', registro, name= 'UserTravelRegistro'),
    path('avatar/', subir_avatar, name= 'UserTravelAvatar'),
    path('perfil/', perfil, name= 'UserTravelPerfil'),
    path('edit_usu/', editar_usuario, name= 'UserTravelEditarUsu'),
    path('testimonio/', testimonio, name= 'UserTravelTestimonio'),
    path('chattestimonio/<int:id>', chatestimonio, name= 'UserTravelChatTestimonio'),
    
]