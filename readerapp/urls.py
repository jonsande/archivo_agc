from django.urls import path, re_path
from readerapp import views

"""El NAME es a lo que llamamos en los links del html, por ejemplo cuando injectamos href="{% url 'home' %}"""
urlpatterns = [
    path('list/<int:year>/<str:month>', views.list_articles, name='list_articles'),
    path('list/<int:year>', views.list_by_year, name='list_by_year'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.dispatch_slug, name="dispatch_slug"),
]