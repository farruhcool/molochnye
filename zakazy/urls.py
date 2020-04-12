from django.conf.urls import url
from zakazy import views

urlpatterns = [
     url('basket_adding/$', views.basket_adding, name='basket_adding'),
     url('checkout/$', views.checkout, name='checkout'),

]