from django.urls import path
from core import views

"""El NAME es a lo que llamamos en los links del html, por ejemplo cuando injectamos href="{% url 'home' %}"""
urlpatterns = [
    path('', views.home, name='Home'),
    path('gindex/', views.gindex, name='Gindex'),
    path('mindex/', views.mindex, name='Mindex'),
    path('contact/', views.contact, name='Contact'),
    path('suscribe/', views.suscribe, name='Suscribe'),
    path('colaborar/', views.colaborar, name='Colaborar'),
    path('admin/', views.admin, name='Admin'),
    path('search/', views.search, name='search'),
]