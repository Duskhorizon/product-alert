from django.contrib import admin
from .models import Produkt
from .models import Surowiec
from .models import Email
# Register your models here.
admin.site.register(Produkt)
admin.site.register(Surowiec)
admin.site.register(Email)