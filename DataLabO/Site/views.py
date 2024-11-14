from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

@login_required
def hello(request):
    return render(request, 'hello.html')
