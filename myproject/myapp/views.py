from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import pandas as pd
import csv
import sqlite3
import os
from myapp.models import LTE


def start(request):
    return render(request, 'myapp/start.html')

def doc(request):
    return render(request, 'myapp/doc.html')

def mobility(request, lte_layer):
    lte = get_object_or_404(LTE, layer=lte_layer)
    return render(request, 'myapp/mobility.html', {'lte': lte})


def lte_list(request):
    ltes = LTE.objects.all()
    return render(request, 'myapp/lte_layer.html', {'ltes': ltes})

def mobility_all(request):
    ltes = LTE.objects.all()
    return render(request, 'myapp/mobility_all.html', {'ltes': ltes})