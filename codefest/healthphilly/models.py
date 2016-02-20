from django.db import models


class CondomDistributor(models.Model):
	longitude = models.CharField(default=='', max_length=300)
	latitude = models.CharField(default=='', max_length=300)
	object_id = models.CharField(default=='', max_length=300)
	site_name = models.CharField(default='', max_length=300)
	hours = models.CharField(default=='', max_length=300)
	address = models.CharField(default=='', max_length=300)
	city = models.CharField(default=='', max_length=300)
	state = models.CharField(default=='', max_length=300)
	zip = models.CharField(default=='', max_length=300)

	pub_date = models.DateTimeField('date published')


class HealthyStartCRC(models.Model):
	longitude = models.CharField(default=='', max_length=300)
	latitude = models.CharField(default=='', max_length=300)
	object_id = models.CharField(default=='', max_length=300)
	facility_name = models.CharField(default='', max_length=300)
	address = models.CharField(default=='', max_length=300)
	city = models.CharField(default=='', max_length=300)
	state = models.CharField(default=='', max_length=300)
	phone = models.CharField(default=='', max_length=300)
	days_open = models.CharField(default=='', max_length=300)
	hours = models.CharField(default=='', max_length=300)
        
	pub_date = models.DateTimeField('date published')


class WICOffice(models.Model):
	longitude = models.CharField(default=='', max_length=300)
	latitude = models.CharField(default=='', max_length=300)
	object_id = models.CharField(default=='', max_length=300)
	loc_name = models.CharField(default='', max_length=300)
	status = models.CharField(default=='', max_length=300)
	score = models.CharField(default=='', max_length=300)
	match_type = models.CharField(default=='', max_length=300)
	match_addr = models.CharField(default=='', max_length=300)
	side = models.CharField(default=='', max_length=300)
	user_fld = models.CharField(default=='', max_length=300)
	addr_type = models.CharField(default=='', max_length=300)
	arc_street = models.CharField(default=='', max_length=300)
	arc_zip = models.CharField(default=='', max_length=300)
	name = models.CharField(default=='', max_length=300)
	address = models.CharField(default=='', max_length=300)
	address_2 = models.CharField(default=='', max_length=300)
	zip = models.CharField(default=='', max_length=300)
	phone_number = models.CharField(default=='', max_length=300)
        
	pub_date = models.DateTimeField('date published')
