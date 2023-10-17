from django.shortcuts import render, HttpResponse
from readerapp.models import Article
import locale
from datetime import date
import calendar


# Create your views here.

locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")

def pifia(request):
    pass

def home(request):

    return render(request, "core/home.html")


def gindex(request):

    #import ipdb;ipdb.set_trace()
    tertulias = Article.objects.order_by('new_cod').all()

    # Construimos un diccionario con los años (como clave) y los meses (como valor) que existe tertulia
    tertu_dict = {}

    for t in tertulias:
        tertu_dict.update({t.new_cod.year: []})

    for t in tertulias:
        if t.new_cod.year in tertu_dict:
                if t.new_cod.month not in tertu_dict[t.new_cod.year]:
                    tertu_dict[t.new_cod.year].append(t.new_cod.month)

    # Construimos un diccionario, reflejo de tertu_dict, pero con los nombre de los meses en vez de números
    verbose_month_dict = tertu_dict

    ## Iterar sobre cada clave del diccionario
    for key in verbose_month_dict.keys():
    ## Iterar sobre cada valor de la lista asociada a la clave
        for i, value in enumerate(verbose_month_dict[key]):
        ## Obtener el nombre del mes correspondiente al número
            month_name = calendar.month_abbr[value].capitalize()
        ## Reemplazar el valor en la lista
            verbose_month_dict[key][i] = month_name
            
    context = {'tertu_dict': tertu_dict, 'verbose_month_dict': verbose_month_dict}
    return render(request, "core/gindex.html", context)

def mindex(request):

    return render(request, "core/mindex.html")


def contact(request):

    return render(request, "core/contact.html")


def suscribe(request):

    return render(request, "core/suscribe.html")

def colaborar(request):

    return render(request, "core/colaborar.html")

def admin(request):

    return render(request, "admin")

# TODO
# + Que los resultados aparezcan ordenados por defecto según fecha
# + Que los resultados se puedan ordenar por fecha ascendente/descendente

def search(request):
    #import ipdb;ipdb.set_trace()
    query = request.GET.get('consulta')
    #if not query:
    #    query = ""
    if query == None:
        tertulias = Article.objects.filter(cuerpo__icontains=' ')
    else:
        tertulias = Article.objects.filter(cuerpo__icontains=query)
    context = {'tertulias': tertulias}
    return render(request, 'core/search.html', context)

