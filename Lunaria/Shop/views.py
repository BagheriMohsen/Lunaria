from django.shortcuts import render

from django.views import generic
#Models
from .models import Product
# Create your views here.


class ShopLists(generic.ListView):
    model   =   Product
    template_name   =   'front/shop.html'


class ShopDetails(generic.DetailView):
    model = Product
    template_name   =   'front/product-single.html'