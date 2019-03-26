from django import forms

from .models import Produkt, Surowiec, Email, Wyrob
from django.forms import formset_factory

class ProduktForm(forms.ModelForm):
    nazwa = forms.CharField(disabled=True)
    minimum = forms.CharField(disabled=True)
    class Meta:
        model = Produkt
        fields = ('nazwa', 'ilosc','minimum',)

class SurowiecForm(forms.ModelForm):
    nazwa = forms.CharField(disabled=True)
    minimum = forms.CharField(disabled=True)
    class Meta:
        model = Surowiec
        fields = ('nazwa', 'ilosc','minimum',)


class WyrobForm(forms.ModelForm):
    nazwa = forms.CharField()
    ilosc = forms.IntegerField()
    class Meta:
        model = Wyrob
        fields = ('nazwa','ilosc',)

class EmailForm(forms.Form):
    name = forms.CharField(
        label='email:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Wpisz nowego maila'
        })
    )
class EmailForm2(forms.ModelForm):
    name = forms.CharField(label='',)
    class Meta:
        model = Email
        fields = ('name',)
    
EmailFormset = formset_factory(EmailForm, extra=1)    