from django.urls import path

from . import views

urlpatterns=[
    path('',views.ShopLists.as_view(),name="shop_lists"),
    path('<pk>',views.ShopDetails.as_view(),name="shop_details")
]