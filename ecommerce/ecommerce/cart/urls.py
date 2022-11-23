from django.urls import path

from ecommerce.cart.views import new_cart_view, update_cart

urlpatterns = (
    path('update/<int:pk>/', update_cart, name='update cart'),
    path('', new_cart_view, name='new cart'),

)
