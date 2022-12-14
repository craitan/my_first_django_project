from django.urls import path

from ecommerce.cart.views import new_cart_view, add_to_cart, remove_from_cart

urlpatterns = (
    path('', new_cart_view, name='new cart'),
    path('add/<int:pk>/', add_to_cart, name='add to cart'),
    path('remove/<int:pk>/', remove_from_cart, name='remove from cart'),
)
