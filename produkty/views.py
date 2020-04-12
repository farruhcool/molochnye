from django.shortcuts import render
from produkty.models import *

def produkt(request, produkt_id):
    produkt = Produkt.objects.get(id=produkt_id)

    session_key=request.session.session_key
    if not session_key:
        request.session.cycle_key()


    print(request.session.session_key)
    return render(request, 'produkty/produkt.html', locals())