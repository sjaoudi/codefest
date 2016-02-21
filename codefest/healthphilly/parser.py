import csv

from .models import Location


with open(path) as f:
    reader = csv.reader(f)

    # 9 condoms 11 healthystart 18 WIC
    if len(reader[0]) == 9:
        parse_condoms(reader[1:])
    else if len(reader[0]) == 11:
        parse_healthystart(reader[1:])
    else if len(reader[0]) == 18:
        parse_WIC(reader[1:])
    else if len(reader[0]) == 12:
        parse_HIV(reader[1:])
    else if len(reader[0]) == 10:
        parse_centers(reader[1:])
    else if len(reader[0]) == 8:
        parse_pp(reader[1:])

def parse_condoms(reader):		
    for row in reader:
	#object, boolean(if object was created)

	obj, created = Location.objects.get_or_create(
       	longitude=row[0]
	latitude=row[1],
	#object_id=row[2],
	site_name=row[3],
	hours=row[4],
	address=row[5],
        #phone_number = #### NEED THIS (google graphs?)
	#state=row[6],
	#city=row[7],
	zipcode=row[8],
	tag = "condoms"

	#add pub date with "now" later
	)

	if created:
            obj.save()

def parse_healthystart(reader):
    for row in reader:
        #object, boolean(if object was created)
        obj, created = Location.objects.get_or_create(
        longitude=row[0]
        latitude=row[1],
        #object_id=row[2],
        facility_name=row[3],
        address=row[4],
        #city=row[7],
        #state=row[6],
        zipcode=row[7]
        phone_number=row[8],
        #days_open=row[9]
        hours=row[10],
        tag = "CRC"

        #add pub date with "now" later
        )
        if created:
            obj.save()


def parse_WIC(reader):
    for row in reader:
        #object, boolean(if object was created)

        extended_address = row[13] + ' ' + row[14]
        obj, created = Location.objects.get_or_create(
        longitude=row[0]
        latitude=row[1],
        #object_id=row[2],
        site_name=row[12],
        address=extended_address,
        #city=row[7],
        #state=row[6],
        zipcode=row[11]
        phone_number=row[8],
        #days_open=row[9]
        hours=row[10],
        tag="WIC"
                    
        #add pub date with "now" later
        )
        if created:
            obj.save()


def parse_HIV(reader):		
    for row in reader:
        #object, boolean(if object was created)
        if row[9]+row[10]:
            other_val=  row[9] + '\n' + row[10]
        else:
            other_val=None
	obj, created = Location.objects.get_or_create(
	longitude=row[0]
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
        #hours= ### NEED THIS (from google graph?)
	address=row[11],
	tag="HIV",
        other = other_val

	#add pub date with "now" later
	)

        if created:
            obj.save()


def parse_centers(reader):		
    for row in reader:
	#object, boolean(if object was created)
	obj, created = Location.objects.get_or_create(
	longitude=row[0]
	latitude=row[1],
	#object_id=row[2],
	site_name=row[3],
	#organization=row[4],
	zipcode=row[5],
	phone_number=row[6],
	#website=row[7], #### IMPLEMENT THIS
        #phone_number2=row[8],
        #special_focus=row[9],
        #special_hours=row[10],
        #hours= ### NEED THIS (from google graph?)
	address=row[11],
	tag="health_center"

	#add pub date with "now" later
	)

	if created:
	    obj.save()


def parse_pp(reader):		
    for row in reader:
        #object, boolean(if object was created)
        obj, created = Location.objects.get_or_create(
        longitude=row[0]
        latitude=row[1],
        site_name=row[3],
        phone_number=row[4],
        #hours= ### NEED THIS (from google graph?)
        address=row[5],
        zipcode=row[6],
        #website=row[7], #### IMPLEMENT THIS
        tag="planned_parenthood"

        #add pub date with "now" later
        )

        if created:
            obj.save()
