from django.contrib import admin
from  .models import PointInteret 
from  .models import  Evenement
from  .models import Commentaire
from  .models import MoyenTransport
from  .models import Region
from  .models import Visiteur
from .models import Admin
# Register your models here.
models_list1=[PointInteret]
admin.site.register(models_list1)
models_list1=[Evenement]
admin.site.register(models_list1)
models_list1=[Commentaire]
admin.site.register(models_list1)
models_list1=[MoyenTransport]
admin.site.register(models_list1)
models_list1=[Region]
admin.site.register(models_list1)
models_list1=[Visiteur]
admin.site.register(models_list1)
models_list1=[Admin]
admin.site.register(models_list1)
