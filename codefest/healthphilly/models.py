from django.db import models


class Location(models.Model):
	longitude = models.CharField(default='', max_length=300)
	latitude = models.CharField(default='', max_length=300)
	site_name = models.CharField(default='', max_length=300)
	phone_number = models.CharField(default='', max_length=15)
	hours = models.CharField(default='', max_length=300)
	address = models.CharField(default='', max_length=300)
	zipcode = models.CharField(default='', max_length=300)
	tag = models.CharField(default='', max_length=300)
	other = models.CharField(default='', max_length=300)

	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.site_name

