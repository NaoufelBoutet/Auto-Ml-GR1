"""
URL configuration for Projet_Plateforme project.
Laurence Berville 2024
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from Authentification  import views as Authentification_views 
from Site import views as Site_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscriptions/', Authentification_views.inscriptions , name='inscription'),
    path('login/', Authentification_views.login_view, name='login'),  # Utilisation de LoginView
    path('hello/', Site_views.hello, name="hello"), # alias et nom de la fonction, ici "hello"
]

