from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def fic(request):
    return HttpResponse("<h1>Hi Welcome to Fictional Books Section!!</h1>")