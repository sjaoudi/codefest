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

def listing(request):
    template = loader.get_template('listing.html')
    return HttpResponse(template.render(request))

def detail(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render(request))
