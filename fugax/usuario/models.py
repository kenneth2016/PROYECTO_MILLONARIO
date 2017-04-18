from django.db import models
class UserTag(models.Model):
	tag= models.ForeignKey('tags.Tag')
	user = models.ForeignKey('django.contrib.auth.User')

