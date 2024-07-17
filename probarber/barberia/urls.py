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
    
    path('servicios', views.servicio, name='servicios'),
    path('crear_servicios', views.crear_servicio, name='crear_servicios'),
    path('editar_servicios/<int:id>', views.editar_servicio, name='editar_servicios'),
    path('eliminar_servicios/<int:id>', views.eliminar_servicio, name='eliminar_servicios'),
    
    path('barberos', views.barbero, name='barberos'),
    path('crear_barberos', views.crear_barberos, name='crear_barberos'),
    path('editar_barberos/<int:id>', views.editar_barberos, name='editar_barberos'),
    path('eliminar_barberos/<int:id>', views.eliminar_barberos, name='eliminar_barberos'),
    
    path('citas', views.cita, name='citas'),
    path('crear_citas', views.crear_citas, name='crear_citas'),
    path('editar_citas/<int:id>', views.editar_citas, name='editar_citas'),
    path('eliminar_citas/<int:id>', views.eliminar_citas, name='eliminar_citas'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
