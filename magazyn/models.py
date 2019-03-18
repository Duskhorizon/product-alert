from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    minimum = models.IntegerField()

class Surowiec(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.DecimalField(decimal_places=2,max_digits=6)
    minimum = models.DecimalField(decimal_places=2,max_digits=6)

