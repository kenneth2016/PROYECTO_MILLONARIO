from django.db import models
from django.contrib.auth.models import User
class UserTag(models.Model):
	tag= models.ForeignKey('tags.Tag')
	user = models.ForeignKey(User)

