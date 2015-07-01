import collections
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONCharField


class PassVault(models.Model):

	user = models.ForeignKey(User, null=True)

	name = models.CharField(max_length=100)
	password = models.CharField(max_length=50)
	category = models.CharField(max_length=50, null=True)
	custom_fields = JSONCharField(load_kwargs={'object_pairs_hook': collections.OrderedDict},
					max_length=1000, null=True)
	description = models.TextField(null=True)

	def __unicode__(self):
		return self.name
