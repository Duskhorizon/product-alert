# -*- coding: utf-8 -*-

from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produkt
from .models import Surowiec
from .models import Wyrob
from .models import Transakcja
from django.forms import ModelForm
import yagmail
from .models import Email
from .forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def magazyn(request):
    produkty = Produkt.objects
    surowce = Surowiec.objects
    wyroby = Wyrob.objects
    formp = MatForm()
    forms = SurForm()
    formw = WyrForm()           
    return render(request,'magazyn.html', {'produkty':produkty,'surowce':surowce,'wyroby':wyroby,'formp':formp,'forms':forms,'formw':formw,})

@login_required
def transakcje(request):
    transakcje = Transakcja.objects
    return render(request,'transakcje.html',{'transakcje':transakcje})

@login_required
def edycja(request):
    produkty = Produkt.objects
    surowce = Surowiec.objects
    return render(request,'edycja.html', {'produkty':produkty,'surowce':surowce})

@login_required
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
            powitanie = "Dzień dobry, w skutek modyfikacji stanów magazynowych mam dla Ciebie informacje o niewystarczających stanach magazynowych następujących produktów:\n "
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

@login_required
def edycja_wyrobow(request):
    WyrobFormSet = modelformset_factory(Wyrob,fields=('nazwa','ilosc',), extra=0)
    if request.method == 'POST':
        formset = WyrobFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():  
            formset.save()
    else:
        formset = WyrobFormSet()
    return render(request, 'edycjawyrobow.html', {'formset': formset})

@login_required
def edycja_emaili(request):
    EmailFormSet = modelformset_factory(Email,form=EmailForm2,fields=('name',), extra=0)
    if request.method == 'POST':
        formset = EmailFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():  
            formset.save()
    else:
        formset = EmailFormSet()
    return render(request, 'edycjamaili.html', {'formset': formset})   


@login_required
def delete_wyrobow(request,wyrob_id):
    wyrob = get_object_or_404(Wyrob, pk=wyrob_id)
    wyrob.delete()
    return redirect('edycjaw')

@login_required
def add_wyrob(request):
    if request.method == "POST":
        form = WyrobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edycjaw')
    else:        
        form = WyrobForm()
    return render(request,'addwyrob.html',{'form':form})

@login_required
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
            powitanie = "Dzień dobry, w skutek modyfikacji stanów magazynowych mam dla Ciebie informacje o niewystarczających stanach magazynowych następujących surowców:\n "
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

@login_required
def delete_surowcow(request,surowiec_id):
    surowiec = get_object_or_404(Surowiec, pk=surowiec_id)
    surowiec.delete()
    return redirect('edycjas')

@login_required
def delete_emaili(request,email_id):
    email = get_object_or_404(Email, pk=email_id)
    email.delete()
    return redirect('edycjam')

@login_required
def add_surowiec(request):
    if request.method == "POST":
        form = NewSurowiecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edycjas')
    else:        
        form = NewSurowiecForm()
    return render(request,'addsurowiec.html',{'form':form})

@login_required
def add_email(request):
    if request.method == "POST":
        form = EmailForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edycjam')
    else:        
        form = EmailForm2()
    return render(request,'addemail.html',{'form':form})

@login_required
def delete_produktow(request,produkt_id):
    produkt = get_object_or_404(Produkt, pk=produkt_id)
    produkt.delete()
    return redirect('edycjap')

@login_required
def add_produkt(request):
    if request.method == "POST":
        form = NewProduktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edycjap')
    else:        
        form = NewProduktForm()
    return render(request,'addprodukt.html',{'form':form})



@login_required
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

@login_required
def mat_produktow(request):
    if request.method == 'POST':
        pk = request.POST['co']
        produkt = get_object_or_404(Produkt, pk=pk)
        if request.POST['dzialanie'] == 'plus':
            produkt.ilosc = produkt.ilosc + int(request.POST['ile'])
            dzialanie = '+'
        else:
            produkt.ilosc = produkt.ilosc - int(request.POST['ile'])
            dzialanie = '-'
        if produkt.ilosc < 0:
            produkt.ilosc = 0                         
        produkt.save()
        brakujace = 0
        transakcja = Transakcja()
        transakcja.kto = request.user
        transakcja.co = produkt.nazwa + ' (produkt)'
        transakcja.ile = dzialanie + request.POST['ile'] + 'szt.'
        transakcja.kiedy = timezone.datetime.now()
        transakcja.save()
        powitanie = "Dzień dobry, w skutek modyfikacji stanów magazynowych mam dla Ciebie informacje o niewystarczających stanach magazynowych następujących produktów:\n "
        modyfikator = "\nPowyższa wiadomość została utworzona ze względu na modyfikacje produktu: %s (%s %s szt.) przez użytkownika %s" %(produkt.nazwa,dzialanie,request.POST['ile'],request.user)
        for produkt in Produkt.objects.all():                
            if produkt.ilosc < produkt.minimum:
                    linijka = produkt.nazwa +' - obecna ilość: '+str(produkt.ilosc) + 'szt, określone minimum na poziomie : ' +str(produkt.minimum) + 'szt.\n'
                    powitanie = powitanie + linijka
                    brakujace = 1
        if brakujace == 1:
            powitanie = powitanie + modyfikator
            to =[]
            for email in Email.objects.all():
                to.append(email.name)                           
            yag = yagmail.SMTP('001010blipblop010101@gmail.com', 'siusiak666')
            to = to
            subject = 'Niewystarczające stany magazynowe!'
            yag.send(to,subject,powitanie)
    return redirect('magazyn')

@login_required
def mat_surowcow(request):
    if request.method == 'POST':
        pk = request.POST['co']
        surowiec = get_object_or_404(Surowiec, pk=pk)
        if request.POST['dzialanie'] == 'plus':
            surowiec.ilosc = surowiec.ilosc + float(request.POST['ile'])
            dzialanie = '+'
        else:
            surowiec.ilosc = surowiec.ilosc - float(request.POST['ile'])
            dzialanie = '-'
        if surowiec.ilosc < 0:
            surowiec.ilosc = 0                     
        surowiec.save()
        brakujace = 0
        transakcja = Transakcja()
        transakcja.kto = request.user
        transakcja.co = surowiec.nazwa + ' (surowiec)'
        transakcja.ile = dzialanie + request.POST['ile'] + 'kg.'
        transakcja.kiedy = timezone.datetime.now()
        transakcja.save()        
        powitanie = "Dzień dobry, w skutek modyfikacji stanów magazynowych mam dla Ciebie informacje o niewystarczających stanach magazynowych następujących surowców:\n "
        modyfikator = "\nPowyższa wiadomość została utworzona ze względu na modyfikacje surowca: %s (%s %s kg.) przez użytkownika %s" %(surowiec.nazwa,dzialanie,request.POST['ile'],request.user)                
        for surowiec in Surowiec.objects.all():                
            if surowiec.ilosc < surowiec.minimum:
                    linijka = surowiec.nazwa +' - obecna ilość: '+str(surowiec.ilosc) + 'kg, określone minimum na poziomie : ' +str(surowiec.minimum) + 'kg.\n'
                    powitanie = powitanie + linijka
                    brakujace = 1
        if brakujace == 1:
            powitanie = powitanie + modyfikator
            to =[]
            for email in Email.objects.all():
                to.append(email.name)                           
            yag = yagmail.SMTP('001010blipblop010101@gmail.com', 'siusiak666')
            to = to
            subject = 'Niewystarczające stany magazynowe!'
            yag.send(to,subject,powitanie)
    return redirect('magazyn')

@login_required
def mat_wyrobow(request):
    if request.method == 'POST':
        pk = request.POST['co']
        wyrob = get_object_or_404(Wyrob, pk=pk)
        if request.POST['dzialanie'] == 'plus':
            wyrob.ilosc = wyrob.ilosc + int(request.POST['ile'])
            dzialanie = '+'
        else:
            wyrob.ilosc = wyrob.ilosc - int(request.POST['ile'])
            dzialanie = '-'
        if wyrob.ilosc < 0:
            wyrob.ilosc = 0                     
        wyrob.save()
        transakcja = Transakcja()
        transakcja.kto = request.user
        transakcja.co = wyrob.nazwa + ' (wyrób)'
        transakcja.ile = dzialanie + request.POST['ile'] + 'szt.'
        transakcja.kiedy = timezone.datetime.now()
        transakcja.save()          
    return redirect('magazyn')

@login_required
def test(request):
    return render(request, 'test.html',)  