from django.conf.urls import url
from polya import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('polya12/', views.polya, name='polya')
]