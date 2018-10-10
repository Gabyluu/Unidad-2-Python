from django.db import models

# Create your models here.

class Pokemon(models.Model):
	  nombre = models.CharField(max length=32)
	  tipo = models.CharField(max lenght=32)
	  energia = models.IntegerField()

	  def __str__(self):
	  		self.nombre