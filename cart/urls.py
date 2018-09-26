from django.urls imort path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='cart')
]
