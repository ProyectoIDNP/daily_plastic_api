from django.db import models

class Category(models.Model):
  name = models.CharField( max_length = 255, null = False, blank = False, verbose_name = 'Nombre' )
  created = models.DateTimeField( auto_now_add = True, verbose_name = 'Fecha de creación' )
  updated = models.DateTimeField( auto_now = True, verbose_name = 'Fecha de actualización' )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Categoría'
    verbose_name_plural = 'Categorías'


class Presentation(models.Model):
  name = models.CharField( max_length = 255, null = False, blank = False, verbose_name = 'Nombre' )
  created = models.DateTimeField( auto_now_add = True, verbose_name = 'Fecha de creación' )
  updated = models.DateTimeField( auto_now = True, verbose_name = 'Fecha de actualización' )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Presentación'
    verbose_name_plural = 'Presentaciones'


class Plastic(models.Model):
  category = models.ForeignKey( Category, blank = False, null = False, on_delete = models.CASCADE, verbose_name = 'Categoría' )
  presentation = models.ForeignKey( Presentation, blank = False, null = False, on_delete = models.CASCADE, verbose_name = 'Presentación' )
  name = models.CharField( max_length = 255, null = False, blank = False, verbose_name = 'Nombre' )
  decomposition_time = models.BigIntegerField( null = True, blank = True, verbose_name = 'Tiempo de descomposición (días)' )
  unit_weight = models.BigIntegerField( null = True, blank = True, verbose_name = 'Peso unitario (gramos)' )
  created = models.DateTimeField( auto_now_add = True, verbose_name = 'Fecha de creación' )
  updated = models.DateTimeField( auto_now = True, verbose_name = 'Fecha de actualización' )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Plástico'
    verbose_name_plural = 'Plásticos'