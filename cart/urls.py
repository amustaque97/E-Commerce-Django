from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='cart'),
    path('add/<int:id>', views.AddItem.as_view(), name='cart-add'),
    path('empty',views.Empty.as_view(), name='cart-empty')
]
