from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    position = models.IntegerField()