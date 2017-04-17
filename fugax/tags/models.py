from django.db import models

# Create your models here.
class Tag(models.Model):
	nombre = models.CharField(max_length=40)

	def __str__(self):
		return "%s" %(self.nombre)