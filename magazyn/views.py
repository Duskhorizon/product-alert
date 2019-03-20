# -*- coding: utf-8 -*-

from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Produkt
from .models import Surowiec
from django.forms import ModelForm
from django.forms import ModelForm, Textarea
import smtplib, ssl

def magazyn(request):
    produkty = Produkt.objects
    surowce = Surowiec.objects
    return render(request,'magazyn.html', {'produkty':produkty,'surowce':surowce})


def edycja(request):
    produkty = Produkt.objects
    surowce = Surowiec.objects
    return render(request,'edycja.html', {'produkty':produkty,'surowce':surowce})


def edycja_produktow(request):
    ProduktFormSet = modelformset_factory(Produkt, fields=('nazwa','ilosc','minimum',), extra=0)
    if request.method == 'POST':
        formset = ProduktFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():  
            formset.save()
            produkty = Produkt.objects.all()
            brakujace = []
            for produkt in produkty:                
                if produkt.ilosc < produkt.minimum:
                    brakujace.append(produkt.nazwa)
            context = ssl.create_default_context()                    
            port = 465
            password = 'siusiak666'
            sender_email = '001010blipblop010101@gmail.com'
            receiver_email = '001010blipblop010101@gmail.com'
            message = ' '.join(brakujace)
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
      
    else:
        formset = ProduktFormSet()
    return render(request, 'edycjaproduktow.html', {'formset': formset}) 

def edycja_surowcow(request):
    SurowiecFormSet = modelformset_factory(Surowiec, fields=('nazwa','ilosc','minimum',),extra=0)
    if request.method == 'POST':
        formset = SurowiecFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():
            formset.save()
            surowce = Surowiec.objects.all()
            brakujace = []
            for surowiec in surowce:                
                if surowiec.ilosc < surowiec.minimum:
                    brakujace.append(surowiec.nazwa)
            context = ssl.create_default_context()                    
            port = 465
            password = 'siusiak666'
            sender_email = '001010blipblop010101@gmail.com'
            receiver_email = '001010blipblop010101@gmail.com'
            message = ' '.join(brakujace)
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            
    else:
        formset = SurowiecFormSet()
    return render(request, 'edycjasurowcow.html', {'formset': formset})    

def alert(request):
    return render(request,'alert.html')