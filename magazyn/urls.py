from django.urls import path
from . import views

urlpatterns = [
    path('', views.magazyn,name='magazyn'),
    path('edycja/', views.edycja,name='edycja'),
    path('edycjap/', views.edycja_produktow,name='edycjap'),
    path('edycjas/', views.edycja_surowcow,name='edycjas'),
    path('edycjaw/', views.edycja_wyrobow,name='edycjaw'),
    path('edycjam/',views.edycja_emaili, name='edycjam'),
    path('deletew/<int:wyrob_id>',views.delete_wyrobow, name='deletew'),
    path('deletee/<int:email_id>',views.delete_emaili, name='deletee'),    
    path('addw/',views.add_wyrob, name='addw'),
    path('deletes/<int:surowiec_id>',views.delete_surowcow, name='deletes'),
    path('adds/',views.add_surowiec, name='adds'),
    path('adde/',views.add_email, name='adde'),
    path('deletep/<int:produkt_id>',views.delete_produktow, name='deletep'),
    path('addp/',views.add_produkt, name='addp'),    
    path('test/',views.test,name='test'),
    path('matp/', views.mat_produktow, name='matp'),
    path('mats/', views.mat_surowcow, name='mats'),
    path('matw/', views.mat_wyrobow, name='matw'),

]
