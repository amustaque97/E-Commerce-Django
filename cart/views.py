from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'cart/index.html'
    context_object_name = 'session'
    
    def get_queryset(self):
        return session.items()
