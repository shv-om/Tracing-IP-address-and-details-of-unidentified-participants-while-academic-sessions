from django.db import models

from registration import models as registered_models


class RandomID(models.Model):
	ruser = models.OneToOneField(registered_models.User, on_delete=models.CASCADE, default=None, null=True)
	random_id = models.CharField(max_length=8, default=None, null=True)


class IPaddress(models.Model):
	ran_id = models.OneToOneField(RandomID, on_delete=models.CASCADE, default=None, null=True)
	ipaddress = models.GenericIPAddressField(null=True)

