from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    # path('products/', views.ProductsView.as_view(), name = 'products'),
    path('',include('django.contrib.auth.urls'), name = 'login'),
    path('sign-up/',views.SignUp.as_view(), name = 'signup'),
    path('',include('django.contrib.auth.urls'), name = 'password_reset'),
    path('login/',include('allauth.urls'), name = 'github'),
]
