from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Home
# from django.views.generic import TemplateView

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'hero'

    def get_queryset(self):
        return Home.objects.all()

class AboutView(generic.TemplateView):
    template_name = 'main/about.html'

class ProductsView(generic.TemplateView):
    template_name = 'main/products.html'

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'
