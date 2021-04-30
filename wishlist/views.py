from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from products.models import ProductsModel

@login_required
def list_add(request, id):
	product = get_object_or_404(ProductsModel, id = id)
	if product.list_favourite.filter(id=request.user.id).exists():
		product.list_favourite.remove(request.user)
	else:
		product.list_favourite.add(request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def wishlist_page(request):
	new = ProductsModel.objects.filter(list_favourite=request.user)
	return render(request, 'templates/wishlist/wishlist.html', {'new':new})