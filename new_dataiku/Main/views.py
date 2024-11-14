from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def accueil(request):
    return render(request, "accueil.html")

@login_required
def projet(request):
    return render(request, "projet.html")