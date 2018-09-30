from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views import generic
from .models import Products
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Products.objects.all()

class DetailView(generic.DetailView):
    # template name
    template_name = 'products/details.html'
    context_object_name = 'product_details'
    slug_field = 'product_slug'

    def get_queryset(self):
        self.title = get_object_or_404(Products, product_slug=self.kwargs['slug'])
        print(self.title)    # for debuggin purposes
        return Products.objects.filter(product_title=self.title)
