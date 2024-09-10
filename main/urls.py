from django.urls import path
from . import views
from main.views import main
from main.views import products

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.products, name='products'),
]
