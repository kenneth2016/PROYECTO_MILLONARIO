from django.db import models
from django.contrib.auth.models import User
class Perfil(models.Model):
	usuario=models.OneToOneField(User)
class UserTag(models.Model):
	tag= models.ForeignKey('tags.Tag')
	user = models.ForeignKey('django.contrib.auth.User')

