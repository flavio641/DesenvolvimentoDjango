from django.contrib import admin
from age.models import Evento

# Register your models here.

class Eventoadmin(admin.ModelAdmin):
    list_display= ('titulo','data_evento','data_criacao')
    list_filter = ('titulo','data_evento',)


admin.site.register(Evento, Eventoadmin)
