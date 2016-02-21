from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import View

from .parser import parsefile, parse_condoms, parse_healthystart
from .models import Location

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render(request))

def searchpage(request):

    parsefile("healthphilly/condom_distribution_sites.csv")

    all_locations = Location.objects.all()
    condom_distributors = all_locations.filter(tag="condoms")
    healthystart = all_locations.filter(tag="CRC")
    wic_office = all_locations.filter(tag="WIC")
    
    jsonobj = {}
    jsonobj['condom_distributors'] = condom_distributors
    jsonobj['healthystart'] = healthystart
    jsonobj['wic_office'] = wic_office
    

    return render(request, 'listing.html', {'jsonobj': jsonobj})

class SearchView(View):
    def get(self, request):
        print dir(request.POST)
        parsefile("healthphilly/condom_distribution_sites.csv")

        all_locations = Location.objects.all()
        condom_distributors = all_locations.filter(tag="condoms")
        healthystart = all_locations.filter(tag="CRC")
        wic_office = all_locations.filter(tag="WIC")
        
        jsonobj = {}
        jsonobj['condom_distributors'] = condom_distributors
        jsonobj['healthystart'] = healthystart
        jsonobj['wic_office'] = wic_office

        return render(request, 'search.html', {'jsonobj': jsonobj})

    def post(self, request):
        clicked_obj = request.POST.get("strID")
        is_checked = request.POST.get("state")

        print is_checked

"""
    locations = {}
    for location in Location.objects.all():
          curr_location = {}
          curr_location["Longitude"] = location.longitude
          curr_location["Latitude"] = location.Latitude
          curr_location["Address"] = location.address
          curr_location["Zipcode"] = location.zipcode
          curr_location["Phone number"] = location.phone_number
          curr_location["Hours"] = location.hours
          curr_location["Tag"] = location.tag
          curr_location["Other"] = location.other
          locations[location.site_name] = curr_location
    return render(request, 'search.html', {"loc": locations})
"""
def listing(request):
    template = loader.get_template('listing.html')
    return HttpResponse(template.render(request))

def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(request))


def map(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render(request))
