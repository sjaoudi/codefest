import csv
import urllib
import json as m_json
from .models import Location
from django.utils import timezone

def get_url(query):
    query = urllib.urlencode ({'q' : query})
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads (response)
    if json['responseData']:
    	search = json ['responseData'] ['results']
    else:
    	search = [{'url':""}]
    return search[0]['url']

def parsefile(path):
	with open(path, 'r') as f:
		reader = csv.reader(f)
		readerlines = [line for line in reader]
		if len(readerlines[0]) == 9:
			parse_condoms(readerlines[1:])
		elif len(readerlines[0]) == 11:
			parse_healthystart(readerlines[1:])
		elif len(readerlines[0]) == 18:
			parse_WIC(readerlines[1:])
		elif len(readerlines[0]) == 12:
			parse_HIV(readerlines[1:])
		elif len(readerlines[0]) == 10:
			parse_centers(readerlines[1:])
		elif len(readerlines[0]) == 8:
                        if path == "healthphilly/Assault.csv":
                            parse_custom(readerlines[1:], "assault")
                        elif path == "healthphilly/Planned_Parenthood.csv":
                            parse_custom(readerlines[1:], "planned_parenthood")

def parse_condoms(reader):
	for row in reader:
                #object, boolean(if object was created)
                url = get_url(row[3])
                phone = 'See website'

		obj, created = Location.objects.get_or_create(
			longitude=row[0],
			latitude=row[1],
			#object_id=row[2],
			site_name=row[3],
			hours=row[4],
			address=row[5],
                        phone_number=phone,
			#state=row[6],
			#city=row[7],
			zipcode=row[8],
			tag = "condoms",
                        website=url,

                        pub_date=timezone.now()
		)

                if created and not Location.objects.get(site_name=obj.site_name).exists():
                        obj.save()


def parse_healthystart(reader):
	for row in reader:
                url = get_url(row[3])
		#object, boolean(if object was created)

		obj, created = Location.objects.get_or_create(
                        longitude=row[0],
                        latitude=row[1],
                        #object_id=row[2],
                        site_name=row[3],
                        address=row[4],
                        #city=row[7],
                        #state=row[6],
                        zipcode=row[7],
                        phone_number=row[8],
                        #days_open=row[9]
                        hours=row[10],
                        tag="CRC",
                        website=url,

                        pub_date=timezone.now()
		)
                if created and not Location.objects.get(site_name=obj.site_name).exists():
                        obj.save()



def parse_WIC(reader):
	for row in reader:
		#object, boolean(if object was created)
                url = get_url(row[13])
                hours_str = 'See website'

		extended_address = row[14] + ' ' + row[15]
		obj, created = Location.objects.get_or_create(
                    longitude=row[0],
                    latitude=row[1],
                    #object_id=row[2],
                    address=extended_address,
                    #state=row[6],
                    #city=row[7],
                    phone_number=row[17],
                    #days_open=row[9]
                    hours=hours_str,
                    zipcode=row[12],
                    site_name=row[13],
                    tag="WIC",
                    website=url,

                    pub_data=timezone.now()
		)
                if created and not Location.objects.get(site_name=obj.site_name).exists():
                        obj.save()



def parse_HIV(reader):
	for row in reader:
		#object, boolean(if object was created)
                url = get_url(row[3])

		if row[9]+row[10]:
			other_val=  row[9] + '\n' + row[10]
		else:
			other_val=None
                hours_str = 'See website'

		obj, created = Location.objects.get_or_create(
                        longitude=row[0],
			latitude=row[1],
                        #object_id=row[2],
                        site_name=row[3],
                        #city=row[4],
                        #state=row[5],
                        zipcode=row[6],
                        phone_number=row[7],
			#phone_number2=row[8],
			#special_focus=row[9],
			#special_hours=row[10],
			hours=hours_str,
                        address=row[11],
                        tag="HIV",
			other=other_val,
                        website=url,

                        pub_data=timezone.now()
		)


                if created and not Location.objects.get(site_name=obj.site_name).exists():
                        obj.save()



def parse_centers(reader):
	for row in reader:
                #object, boolean(if object was created)
                hours_str = 'See website'

		obj, created = Location.objects.get_or_create(
                        longitude=row[0],
                        latitude=row[1],
                        #object_id=row[2],
                        site_name=row[3],
                        #organization=row[4],
                        zipcode=row[5],
                        phone_number=row[6],
                        website=row[7],
			hours=hours_str,
                        address=row[9],
                        tag="health_center",

                        pub_data=timezone.now()
		)

                if created and not Location.objects.get(site_name=obj.site_name).exists():
                        obj.save()



def parse_custom(reader, _tag):
	for row in reader:
		#object, boolean(if object was created)
                hours_str = 'See website'

		obj, created = Location.objects.get_or_create(
                        longitude=row[0],
                        latitude=row[1],
                        site_name=row[2],
                        phone_number=row[3],
                        hours=hours_str,
                        address=row[5],
                        zipcode=row[6],
                        website=row[7],
                        tag=_tag,

                        pub_data=timezone.now()
		)

                if created and not Location.objects.get(site_name=obj.site_name).exists():
                        obj.save()
