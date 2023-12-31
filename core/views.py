from django.shortcuts import render, HttpResponse
from readerapp.models import Article
from .models import HomeConfig
import locale
from datetime import date
import calendar


# Create your views here.

locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")

#def home(request):
#
#    return render(request, "core/home.html")

def home(request):
    #configuracion = HomeConfig.objects.first() # Obtener la primera instancia del modelo
    #configuracion = HomePageConfig.obtener_configuracion_sitio()
    configuracion = HomeConfig.load()
    context = {'configuracion': configuracion}
    return render(request, 'core/home.html', context)


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


def search(request):
    from django.db.models import Count

    #import ipdb;ipdb.set_trace()

    query = request.GET.get('consulta')

    if query == None:
        tertulias = Article.objects.filter(cuerpo__icontains=' ')
        context = {'tertulias': tertulias, 'query': query}
        return render(request, 'core/search.html', context)
    
    else:
        tertulias = Article.objects.filter(cuerpo__icontains=query)

        tertu_dict = {}

        for i in tertulias:
            body = i.cuerpo.lower()
            counter = body.count(query.lower())
            tertu_dict.update({i: counter})

        context = {'tertulias': tertulias, 'tertu_dict': tertu_dict, 'query': query}
        return render(request, 'core/search.html', context)
    
