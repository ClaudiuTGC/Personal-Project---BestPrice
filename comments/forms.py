from django import forms
from .models import CommentsModel

class CommentsForm(forms.ModelForm):
	class Meta:
		model = CommentsModel
		fields = [
			'text',
		]