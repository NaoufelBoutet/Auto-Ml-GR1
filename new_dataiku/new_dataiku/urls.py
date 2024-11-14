"""
URL configuration for new_dataiku project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Authentification import views as authviews
from Main import views as Mainviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', authviews.connexion , name='connexion'),
    path('inscription/', authviews.inscription , name='inscription'),
    path('deconnexion/', authviews.deconnexion , name='deconnexion'),
    path('', Mainviews.accueil , name='accueil'),
    path('accueil/', Mainviews.accueil , name='accueil'),
    path('projet/', Mainviews.projet , name='projet'),
]
