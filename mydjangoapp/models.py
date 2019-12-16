from django.db import models

class django_model(models.Model):
   id = models.IntegerField
   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   email = models.CharField(max_length = 50)

