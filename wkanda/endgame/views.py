from django.shortcuts import render
from django.http import HttpResponse
from .models import Avengers

# Create your views here.


def index(request):
    data = [{'name': x.name, 'weapon': x.weapon, 'avtar': x.avatar} for x in Avengers.objects.all()]
    return HttpResponse(data)
