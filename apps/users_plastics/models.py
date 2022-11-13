from django.db import models
from django.contrib.auth.models import User
from apps.plastics.models import Plastic

class Origin(models.Model):
  name = models.CharField( max_length = 255, null = False, blank = False, verbose_name = 'Nombre' )
  created = models.DateTimeField( auto_now_add = True, verbose_name = 'Fecha de creación' )
  updated = models.DateTimeField( auto_now = True, verbose_name = 'Fecha de actualización' )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Origen'
    verbose_name_plural = 'Origenes'


class User_Plastic(models.Model):
  user = models.ForeignKey( User, blank = False, null = False, on_delete = models.CASCADE, verbose_name = 'Usuario' )
  plastic = models.ForeignKey( Plastic, blank = False, null = False, on_delete = models.CASCADE, verbose_name = 'Plástico' )
  origin = models.ForeignKey( Origin, blank = False, null = False, on_delete = models.CASCADE, verbose_name = 'Origen' )
  image = models.ImageField( upload_to = 'plastic/', max_length=255, null = True, blank = True, verbose_name = 'Imagen')
  description = models.CharField( max_length = 500, null = False, blank = False, verbose_name = 'Descripción' )
  units = models.BigIntegerField( null = True, blank = True, verbose_name = 'Unidades' )
  created = models.DateTimeField( auto_now_add = True, verbose_name = 'Fecha Creación' )
  updated = models.DateTimeField( auto_now = True, verbose_name = 'Fecha Actualización' )

  def __str__(self):
    return f'{self.units} unid. {self.plastic} de {self.user}'

  class Meta:
    verbose_name = 'Plastico de usuario'
    verbose_name_plural = 'Plasticos de usuario'