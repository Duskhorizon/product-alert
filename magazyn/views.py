# -*- coding: utf-8 -*-

from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Produkt
from .models import Surowiec
from .forms import ProduktForm, SurowiecForm
from django.forms import ModelForm
import yagmail
from .forms import EmailFormset
from .forms import EmailForm2
from .models import Email

def magazyn(request):
    produkty = Produkt.objects
    surowce = Surowiec.objects
    return render(request,'magazyn.html', {'produkty':produkty,'surowce':surowce})


def edycja(request):
    produkty = Produkt.objects
    surowce = Surowiec.objects
    return render(request,'edycja.html', {'produkty':produkty,'surowce':surowce})


def edycja_produktow(request):
    if request.user.is_superuser:
        ProduktFormSet = modelformset_factory(Produkt,fields=('nazwa','ilosc','minimum',), extra=0)
    else:
        ProduktFormSet = modelformset_factory(Produkt, form=ProduktForm, fields=('nazwa','ilosc','minimum',), extra=0)      
    if request.method == 'POST':
        formset = ProduktFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():  
            formset.save()
            brakujace = 0
            powitanie = "Dzień dobry, w skutek modyfikacji stanów magazynowych mam dla Ciebie o informacje o niewystarczających stanach magazynowych następujących produktów:\n "
            for produkt in Produkt.objects.all():                
                if produkt.ilosc < produkt.minimum:
                    linijka = produkt.nazwa +' - obecna ilość: '+str(produkt.ilosc) + 'szt, określone minimum na poziomie : ' +str(produkt.minimum) + 'szt.\n'
                    powitanie = powitanie + linijka
                    brakujace = 1
            if brakujace == 1:
                to =[]
                for email in Email.objects.all():
                    to.append(email.name)                           
                yag = yagmail.SMTP('001010blipblop010101@gmail.com', 'siusiak666')
                to = to
                subject = 'Niewystarczające stany magazynowe!'
                yag.send(to,subject,powitanie)
        
    else:
        formset = ProduktFormSet()
    return render(request, 'edycjaproduktow.html', {'formset': formset}) 

def edycja_surowcow(request):
    if request.user.is_superuser:
        SurowiecFormSet = modelformset_factory(Surowiec,fields=('nazwa','ilosc','minimum',), extra=0)
    else:
        SurowiecFormSet = modelformset_factory(Surowiec, form=SurowiecForm, fields=('nazwa','ilosc','minimum',), extra=0)   
    if request.method == 'POST':
        formset = SurowiecFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():
            formset.save()
            brakujace = 0
            powitanie = "Dzień dobry, w skutek modyfikacji stanów magazynowych mam dla Ciebie o informacje o niewystarczających stanach magazynowych następujących surowców:\n "
            for surowiec in Surowiec.objects.all():                
                if surowiec.ilosc < surowiec.minimum:
                    linijka = surowiec.nazwa +' - obecna ilość: '+str(surowiec.ilosc) + 'kg, określone minimum na poziomie : ' +str(surowiec.minimum) + 'kg.\n'
                    powitanie = powitanie + linijka
                    brakujace = 1
            if brakujace == 1:       
                yag = yagmail.SMTP('001010blipblop010101@gmail.com', 'siusiak666')
                to = '001010blipblop010101@gmail.com'
                subject = 'Niewystarczające stany magazynowe!'
                yag.send(to,subject,powitanie)
            
    else:
        formset = SurowiecFormSet()
    return render(request, 'edycjasurowcow.html', {'formset': formset})    

def emaile(request):
    EmailFormSet2 = modelformset_factory(Email,form=EmailForm2,fields=('name',), extra=0)
    template_name = 'testowy.html'
    if request.method == 'GET':
        formset = EmailFormset()
    elif request.method == 'POST':
        formset = EmailFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save Email instance
                if name:
                    Email(name=name).save()
            # once all Emails are saved, redirect to Email list view
            return redirect('magazyn')
    return render(request, template_name, {
        'formset': formset,
        'emailformset': EmailFormSet2,
    })