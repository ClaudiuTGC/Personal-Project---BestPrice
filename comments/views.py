from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
from products.models import *

def comments_view(request, id):
	component = get_object_or_404(ProductsModel, id = id)
	comments = CommentsModel.objects.filter(component = component).order_by('-id')

	if request.method == 'POST':
		comment_form = CommentsForm(request.POST or None)
		if comment_form.is_valid():
			text = request.POST.get('text')
			comment_form = CommentsModel.objects.create(component=component, user=request.user, text=text)
			comment_form.save()
			return HttpResponseRedirect(component.get_absolute_url())
	else:
		comment_form = CommentsForm()
	context = {'object':component, 'object2':comments, 'comment_form':comment_form}
	return render(request, 'templates/comments/comments.html', context)