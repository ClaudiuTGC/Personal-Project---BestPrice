from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home_page(request):
	fields = CategoryModel.objects.all()
	context = {'object': fields}
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid:
			form.save()
		else:
			form = CategoryForm(request.POST)
	return render(request, 'templates/home/home.html', context)
