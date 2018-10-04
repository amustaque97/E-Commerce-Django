from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from products.models import Products
from django.core import serializers
from django.urls import reverse_lazy, reverse
import json

CART = 'cart'

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'cart/index.html'
    context_object_name = 'session'

    def get_queryset(self):
        self.cart = None
        try:
            if CART in self.request.session.keys():
                self.cart =  self.request.session[CART]
        except Exception as e:
            self.cart = None
        return self.cart


# Add item to the cart
class AddItem(generic.ListView):
    template_name = 'cart/index.html'
    context_object_name = 'session'

    def get_queryset(self):
        # item details
        self.product = serializers.serialize("json",Products.objects.filter(pk=self.kwargs['id']))
        # json conversion
        self.product = json.loads(self.product[1:-1])
        self.pk = self.product['pk']
        self.quantity = 1
        self.price = self.product['fields']['product_price']
        # make new object for addtion to the CART dictionary
        self.item = {
            'price': self.price,
            'quantity': self.quantity
        }
        if CART not in self.request.session.keys():
            self.request.session.clear()
            self.request.session[CART] = {}
            self.request.session[CART][self.pk] = self.item
            self.request.session.modified = True
        else:
            # cart is intialized but no item is present
            if str(self.pk) not in self.request.session[CART].keys():
                self.request.session[CART][self.pk] = self.item
                self.request.session.modified = True
            else:
                # if item is present, update the quantity
                self.request.session[CART][str(self.pk)]['quantity'] += 1
                self.request.session.modified = True
        return self.request.session[CART].items()

class Empty(generic.RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'cart'

    def get_redirect_url(self, *args, **kwargs):
        try:
            del self.request.session[CART]
        except Exception as e:
            pass
        return super().get_redirect_url(*args, **kwargs)
