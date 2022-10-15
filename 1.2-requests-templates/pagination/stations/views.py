import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(str(settings.BUS_STATION_CSV), 'r', encoding='utf-8') as file_obj:
        data = list(csv.DictReader(file_obj, delimiter=','))

    paginator = Paginator(data, 10)
    page_number = int(request.GET.get("page", 1))

    context = {
        'bus_stations': paginator.get_page(page_number),
        'page': paginator.get_page(page_number)
    }
    return render(request, 'stations/index.html', context)
