from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Location

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render(request))

def searchpage(request):
    all_locations = Location.objects.all()
    condom_distributors = all_locations.filter(tag="condom_distributor")
    healthystart = all_locations.filter(tag="healthystart")
    wic_office = all_locations.filter(tag="wic_office")
    
    jsonobj = {}
    jsonobj['condom_distributors'] = condom_distributors
    jsonobj['healthystart'] = healthystart
    jsonobj['wic_office'] = wic_office
     
    return render(request, 'search.html', jsonobj)

def listing(request):
    template = loader.get_template('listing.html')
    return HttpResponse(template.render(request))

def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(request))
