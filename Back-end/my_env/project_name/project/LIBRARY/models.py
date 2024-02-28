from django.db import models

class bookss(models.Model):
    book_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    
    
# Create your models here.
