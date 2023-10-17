from django.shortcuts import render, get_object_or_404
from readerapp.models import Article, Slug
from datetime import date
import calendar
# Para la generación de pdf:



# Create your views here.


def list_articles(request, year, month):
    #import ipdb;ipdb.set_trace()

    # Transformamos el str month en número:
    num_month = list(calendar.month_abbr).index(month.lower())

    start = date(year, num_month, 1)
    day = calendar.monthrange(year, num_month)
    end = date(year, num_month, day[1])
    tertulias = Article.objects.order_by('new_cod').filter(new_cod__gte=start, new_cod__lte=end).all()
    head = month + ' ' + str(year)
    context = {'tertulias': tertulias, 'head': head}
    return render(request, "readerapp/tertulias-list.html", context)


def list_by_year(request, year):
    tertulias = Article.objects.order_by('new_cod').filter(new_cod__year=year).all()
    head = 'Año ' + str(year)
    context = {'tertulias': tertulias, 'head': head}
    return render(request, "readerapp/tertulias-list.html", context)


def dispatch_slug(request, slug):
    slug = get_object_or_404(Slug, slug=slug)
    qs = Article.objects.filter(slug=slug)
    if qs.exists():
        tertulia = qs[0]
    return render(request, "readerapp/tertulia-single.html", locals())



