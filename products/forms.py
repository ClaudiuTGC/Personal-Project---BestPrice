from django import forms
from .models import *

class ProductsForm(forms.ModelForm):
	model = ProductsModel
	class Meta:
		fields = [
			'name',
			'price',
			'link'
		]