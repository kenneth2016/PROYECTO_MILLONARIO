from django.db import models

# Create your models here.
class Avatar(models.Model):
	avatar = models.ImageField(upload_to = 'avatar_folder/')
