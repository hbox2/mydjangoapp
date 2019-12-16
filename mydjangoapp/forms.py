from django import forms
from .models import django_model

class UserForm(forms.ModelForm):
	first_name= forms.CharField(max_length=100)
	last_name= forms.CharField(max_length=100)
	email= forms.EmailField()

	class Meta:
		model = django_model
		db_table = "django_table"
		fields = ('first_name','last_name','email',)

class RecordForm(forms.Form):
	id = forms.CharField(max_length=5)

	class Meta:
		model = django_model
		db_table = "django_table"
		fields = ('id',)
