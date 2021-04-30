from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from django.db.models import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
    Transform,
)
from products.models import *
from django.urls import reverse

class CommentsModel(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
	component = models.ForeignKey(ProductsModel,on_delete=models.SET_NULL, null=True)
	text = models.TextField(null=False) 
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '%s %s' % (self.component.name, self.user.username)
