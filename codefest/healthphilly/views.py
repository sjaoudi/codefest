# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.core import serializers

from .parser import parsefile, parse_condoms, parse_healthystart
from .models import Location

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def about(request):
    template = loader.get_template('about.html')

    if not Location.objects.filter(tag="condoms"):
        parsefile("healthphilly/Condom_distribution_sites.csv")
    if not Location.objects.filter(tag="CRC"):
        parsefile("healthphilly/Healthy_Start_CRCs.csv")
    if not Location.objects.filter(tag="WIC"):
        parsefile("healthphilly/WIC_Offices.csv")
    if not Location.objects.filter(tag="health_center"):
        parsefile("healthphilly/Health_Centers.csv")
    if not Location.objects.filter(tag="HIV"):
        parsefile("healthphilly/RW_HIV_Treatment_Centers.csv")
    if not Location.objects.filter(tag="assault"):
        parsefile("healthphilly/Assault.csv")
    if not Location.objects.filter(tag="planned_parenthood"):
        parsefile("healthphilly/Planned_Parenthood.csv")

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
        print "IN GET!"
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
        print "IN POST"
        clicked_obj = request.POST.get("strID")
        is_checked = request.POST.get("state")

        context = {}
        if clicked_obj == "condom":
            condom_distributors = Location.objects.all()
            context["locations"] = condom_distributors
            if is_checked == "1":
                context["add"] = True
            else:
                context["add"] = False

        locations = Location.objects.all()
        #print context
        #print type(request) #WSGI
        #print type("search.html") #str
        #print type(context) #RequestContext

        # return render(request, 'search.html', context)
        return render(request, 'search.html', context)


        # return render_to_response('search.html', context_instance = request_context)
        #print clicked_obj




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
    locations = Location.objects.all()
    context = RequestContext(request, {
        'locations': locations,
    })
    return render_to_response('map.html', context_instance = context)

def credits(request):
    template = loader.get_template('credits.html')
    return HttpResponse(template.render(request))
