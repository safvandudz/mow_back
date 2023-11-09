from django.contrib import admin
from django.urls import path, include

from api.v1.customer import views


urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),  
    path('categories/', views.categories),
    path('restaurants/', views.restaurants),
    path('food/category/<int:id>/', views.food_category),
    path('foods/<int:id>/', views.foods),
    path('cart/', views.cart),
    path('cart/add/', views.cart_add),
    path('cart/plus/', views.cart_plus),
    path('cart/minus/', views.cart_minus),
    path('place/order/', views.place_order),
    path('address/', views.address),
    path('orders/', views.orders),

]