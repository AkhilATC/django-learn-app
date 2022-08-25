from django.shortcuts import render
from django.http import HttpResponse
from .models import Avengers
from django.template import loader

# Create your views here.


def index(request):
    data = [{'name': x.name, 'weapon': x.weapon, 'avtar': x.avatar} for x in Avengers.objects.all()]
    return HttpResponse(data)


def temp_view(request):
    temp = loader.get_template("endgame/index.html")
    ctx = {'name': 'akhil'} # context object
    return HttpResponse(temp.render(ctx, request))


def temp_view_advance(request):
    return render(request, 'endgame/index.html', {})