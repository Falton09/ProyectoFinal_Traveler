from django.contrib import admin
from AppTravel.models import NombreDestino, NombreHotel, Vuelo, Hotel
from UserTravel.models import Avatar, Testimonio

#Admin de AppTravel
admin.site.register(Vuelo)
admin.site.register(Hotel)
admin.site.register(NombreDestino)
admin.site.register(NombreHotel)


#Admin de UserTravel
admin.site.register(Avatar)
admin.site.register(Testimonio)
