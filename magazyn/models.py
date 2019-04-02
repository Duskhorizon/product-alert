from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    minimum = models.IntegerField()
    objects = models.Manager()
    def __str__(self):
        return self.nazwa 

class Surowiec(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.FloatField()
    minimum = models.FloatField()
    objects = models.Manager()
    def __str__(self):
        return self.nazwa  

class Wyrob(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    objects = models.Manager()   
    def __str__(self):
        return self.nazwa 
        
class Email(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager() 
    class Meta:
        db_table = 'email'

    def __str__(self):
        return self.name

class Transakcja(models.Model):
    kto = models.CharField(max_length=200)
    co = models.CharField(max_length=200)
    ile = models.CharField(max_length=200)
    kiedy = models.DateTimeField()
    objects = models.Manager()



