from django.urls import path
from . import views

urlpatterns=[
    path('cadastro/', views.Cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('recuperasenha/', views.Recupera, name='recupera'),
    
    

]