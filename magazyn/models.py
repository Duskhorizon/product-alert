from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()
    minimum = models.IntegerField()

class Surowiec(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.FloatField()
    minimum = models.FloatField()

class Wyrob(models.Model):
    nazwa = models.CharField(max_length=200)
    ilosc = models.IntegerField()  

class Email(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        db_table = 'email'

    def __str__(self):
        return self.name


