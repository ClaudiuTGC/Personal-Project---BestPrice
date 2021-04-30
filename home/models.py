from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
	name  = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True)
	url_image = models.URLField(null=True, blank=True)

	def get_absolute_url(self):
		return f"/products/{self.name}/"

	def __str__(self):
		return self.name