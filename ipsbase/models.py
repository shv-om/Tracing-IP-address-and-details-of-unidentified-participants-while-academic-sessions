from django.db import models

from registration import models as registered_models


class RandomID(models.Model):
	ruser = models.OneToOneField(registered_models.User, on_delete=models.CASCADE, primary_key=True)
	random_id = models.CharField(max_length=8, default=None, null=True)
