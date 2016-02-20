from django.db import models

# Create your models here.
class CondomDistributor(models.Model):
	business_name = models.CharField(default='', max_length=300)
	pub_date = models.DateTimeField('date published')
	longitude = models.CharField(default='')