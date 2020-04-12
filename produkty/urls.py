from django.conf.urls import url
from produkty import views

urlpatterns = [
     url('produkt/(?P<produkt_id>\w+)/$', views.produkt, name='produkt')
]