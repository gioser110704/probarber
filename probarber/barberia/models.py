# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Barbero(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    especialidad = models.ForeignKey('Especialidad', models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' 

    class Meta:
        managed = False
        db_table = 'barbero'
        
    def delete1 (self, using = None, keep_parents = False):
            super().delete()
        
    


class Cita(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, blank=True, null=True)
    barbero = models.ForeignKey(Barbero, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.CharField(max_length=10, blank=True, null=True)
    servicio = models.ForeignKey('Servicio', models.PROTECT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'
        
    def delete1 (self, using = None, keep_parents = False):
            super().delete()


class Cliente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True, verbose_name = 'Fecha')
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido + '  ' '  V-' + str(self.cedula)


    class Meta:
        managed = False
        db_table = 'cliente'
        
    def delete1 (self, using = None, keep_parents = False):
            super().delete()



class Especialidad(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
         fila= self.descripcion
         return fila

    class Meta:
        managed = False
        db_table = 'especialidad'
        
    def delete1 (self, using = None, keep_parents = False):
            super().delete()
        



class Pago(models.Model):
    cita = models.ForeignKey(Cita, models.DO_NOTHING, blank=True, null=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Servicio(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    duracion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    
    def __str__(self):
         fila= self.nombre
         return fila

    class Meta:
        managed = False
        db_table = 'servicio'
        
    def delete1 (self, using = None, keep_parents = False):
            super().delete()
