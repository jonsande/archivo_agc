from django.contrib import admin
from .models import HomeConfig

# Register your models here.

#class HomeAdmin(admin.ModelAdmin):
#    list_display = ['texto_portada']


admin.site.register(HomeConfig)