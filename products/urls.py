from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.IndexView.as_view(), name='products'),
    path('details/<slug:slug>', views.DetailView.as_view(), name='detail-page'),
]
