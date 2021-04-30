from django.db import models
from django.contrib.auth.models import User
from home.models import CategoryModel
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from django.db.models import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
    Transform,
)
from django.urls import reverse

class ProductsModel(models.Model):
	category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
	name  = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	link  = models.URLField()
	list_favourite = models.ManyToManyField(User, related_name = 'favourite', default = None, blank = True)
	image = models.ImageField(null=True, blank=True)

	def get_absolute_url(self):
		return reverse('product', args=[str(self.id)])