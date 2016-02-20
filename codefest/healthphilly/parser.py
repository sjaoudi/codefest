import csv

from .models import CondomDistributor


with open(path) as f:
	reader = csv.reader(f)

	if len(reader[0]) == 10:
		parse_condoms(reader[1:])



def parse_condoms(reader):		
	for row in reader:
		#object, boolean(if object was created)

		obj, created = CondomDistributor.objects.get_or_create(
			longitude=row[0]
			latitude=row[1],
			object_id=row[2],
			site_name=row[3],
			hours=row[4],
			address=row[5],
			state=row[6],
			city=row[7],
			zip=row[8],
			#add pub date with "now" later
			)
		if created:
			obj.save()



