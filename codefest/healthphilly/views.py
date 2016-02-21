from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render(request))

def searchpage(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render(request))

def listing(request):
    template = loader.get_template('listing.html')
    return HttpResponse(template.render(request))

def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(request))

def map(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render(request))
