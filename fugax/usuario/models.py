from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
class Perfil(models.Model):
	usuario=models.OneToOneField(User)
>>>>>>> origin/master
class UserTag(models.Model):
	tag= models.ForeignKey('tags.Tag')
	user = models.ForeignKey(User)

