from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def products_page(request, id):
	categories = CategoryModel.objects.get(name = id)
	fields = ProductsModel.objects.all()
	context = {'object': fields, 'object2': categories}
	if request.user.is_superuser:
		if request.method == 'POST':
			form = ProductsForm(request.POST)
			if form.is_valid:
				form.save()
				messages.success(request, 'Ai inregistrat cu succes o noua componenta!')
			else:
				form = ProductsForm(request.POST)
	return render(request, 'templates/products/products.html', context)