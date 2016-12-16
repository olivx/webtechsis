from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def license_prennity(request):
    return render(request, 'license_perennity.html')




