from django.db import models
from django.contrib.auth.models import User


class WebLinks(models.Model):

	user = models.ForeignKey(User, null=True)
	title = models.CharField(max_length=150)
	url = models.URLField(max_length=200)
	category = models.CharField(max_length=30, null=True)
	description = models.TextField(null=True)

	def __unicode__(self):
		return self.title
