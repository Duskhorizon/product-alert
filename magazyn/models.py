from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    minimum = models.IntegerField()
    objects = models.Manager() 

class Surowiec(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.FloatField()
    minimum = models.FloatField()
    objects = models.Manager() 

class Wyrob(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    objects = models.Manager()   

class Email(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager() 
    class Meta:
        db_table = 'email'

    def __str__(self):
        return self.name


