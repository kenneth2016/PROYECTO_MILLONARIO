from django import forms
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
	class Enter:
		model= User
		fields= [
		'nombre'
		'email']