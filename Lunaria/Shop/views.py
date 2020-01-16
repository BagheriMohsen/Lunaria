from django.shortcuts import render

from django.views import generic
#Models
from .models import Shop
# Create your views here.


class ShopLists(generic.ListView):
    model   =   Shop
    template_name   =   'front/shop.html'