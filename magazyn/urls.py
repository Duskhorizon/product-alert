from django.urls import path
from . import views

urlpatterns = [
    path('', views.magazyn,name='magazyn'),
    path('edycja/', views.edycja,name='edycja'),
    path('edycjap/', views.edycja_produktow,name='edycjap'),
    path('edycjas/', views.edycja_surowcow,name='edycjas'),
    path('test/',views.emaile, name='edycjam'),
]
