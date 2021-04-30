from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
	model = CategoryModel
	class Meta:
		fields = [
			'category',
			'name'
		]