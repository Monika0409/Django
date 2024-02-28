from django.db import models

# Create your models here.

class Countrys(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Citys(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Countrys, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()



class Subject1s(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    status = models.BooleanField()



class Markss(models.Model):
    subject = models.CharField(max_length=30)
    marks = models.PositiveIntegerField()
    
    #'subject','marks'
    