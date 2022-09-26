from django.contrib.auth.views import LogoutView
from django.urls import path

from UserTravel.views import *

urlpatterns = [
    path('login/', login_request, name='UserTravelLogin'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='UserTravelLogout'),
    path('registro/', registro, name= 'UserTravelRegistro'),
    path('avatar/', subir_avatar, name= 'UserTravelAvatar'),
    path('perfil/', perfil, name= 'UserTravelPerfil'),
    path('cambiar_contrasena/', cambiar_contrasena, name= 'UserTravelCambiarContrasena'),
    path('edit_usu/', editar_usuario, name= 'UserTravelEditarUsu'),
    path('testimonio/', testimonio, name= 'UserTravelTestimonio'),
    path('ver_mi_testimonios/', ver_mi_testimonios, name= 'UserTravelVerMiTestimonio'),
    path('ver_testimonios/', ver_testimonios, name= 'UserTravelVerTestimonios'),
    path('edit_testimonio/<int:id>', edit_testimonio, name= 'UserTravelEditarTestimonio'),
    path('eliminar_testimonio/<int:id>', eliminar_testimonio, name= 'UserTravelEliminarTestimonio'),
    path('chattestimonio/<int:id>', chatestimonio, name= 'UserTravelChatTestimonio'),
    path('ver_comentarios/', ver_comentarios, name= 'UserTravelVerComentarios'),
    path('edit_comentario/<int:id>', edit_comentario, name= 'UserTravelEditarComentarios'),
    path('eliminar_comentario/<int:id>', eliminar_comentario, name= 'UserTravelEliminarComentarios'),

    
]