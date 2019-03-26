from django.urls import path
from . import views

urlpatterns = [
    path('', views.magazyn,name='magazyn'),
    path('edycja/', views.edycja,name='edycja'),
    path('edycjap/', views.edycja_produktow,name='edycjap'),
    path('edycjas/', views.edycja_surowcow,name='edycjas'),
    path('edycjaw/', views.edycja_wyrobow,name='edycjaw'),
    path('edycjam/',views.emaile, name='edycjam'),
    path('deletew/<int:wyrob_id>',views.delete_wyrobow, name='deletew'),
    path('addw/',views.add_wyrob, name='addw'),
    path('test/',views.test,name='test'),
]
