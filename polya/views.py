from django.shortcuts import render
from django.http import HttpResponse
from produkty.models import *




def polya(request):
    return render(request, 'polya/polya.html',locals())

def home(request):
    produkts_images = ProduktImage.objects.filter(is_active=True, is_main=True)
    produkt = Produkt.objects.filter(is_active=True)
    return render(request, 'polya/home.html',locals())
