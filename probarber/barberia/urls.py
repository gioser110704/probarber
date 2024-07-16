from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
          
    #URLS de inicio
    path('', views.inicio , name='inicio'),
    
    path('menu_clientes', views.menu_clientes, name='menu_clientes'),
    path('crear_clientes', views.crear_clientes, name='crear_clientes'),
    path('editar_clientes/<str:cedula>', views.editar_clientes, name='editar_clientes'), #Recibe un string que ingresa el cedula del cliente a editar
    path('eliminar_clientes/<str:cedula>', views.eliminar_clientes, name='eliminar_clientes'), #Recibe un string que ingresa el cedula del cliente a eliminar
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
