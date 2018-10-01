from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from products.models import Products
from django.core import serializers
from django.urls import reverse_lazy


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'cart/index.html'
    context_object_name = 'session'
    
    def get_queryset(self):
    	try:
    		if 'cart' not in self.request.session:
    			return "No Item in the cart"

    	except Exception as e:
    		return self.request.session.items()


# Add item to the cart
class AddItem(generic.ListView):
	model = Products
	template_name = 'cart/index.html'
	context_object_name = 'session'


	def get_queryset(self):
		self.product = serializers.serialize("json",Products.objects.filter(id=self.kwargs['id']))
		print(self.product)
		self.request.session['cart'] = self.product
		return self.request.session.items()

# Empty your cart
class Empty(generic.ListView):
	template_name = 'cart/index.html'
	context_object_name = 'session'

	def get_queryset(self):
		try:
			self.request.session.clear()
			return reverse_lazy(cart)
		except Exception as e:
			return "Error in Removing items."

