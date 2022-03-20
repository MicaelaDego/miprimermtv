from html.entities import entitydefs
from django.db import models
from datetime import datetime

# Create your models here.
class Familia (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    DNI = models.IntegerField(primary_key=True)
    edad = models.DateField
