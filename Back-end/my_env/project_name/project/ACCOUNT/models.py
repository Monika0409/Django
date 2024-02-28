from django.db import models


class finances(models.Model):
    head_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    

    
# Create your models here.
