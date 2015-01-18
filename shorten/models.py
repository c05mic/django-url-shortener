from django.db import models

class Url(models.Model):
	"""
	Model representing each url shortened. The primary key (auto-generated) becomes
	the shortened url.
	"""

	url = models.TextField()
	date_created = models.DateTimeField()
	date_last_accessed = models.DateTimeField(null=True)
	visits = models.IntegerField(null=True)