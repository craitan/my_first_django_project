from django.urls import path

from ecommerce.store.views import store_view, checkout_view

urlpatterns = (
    path('', store_view, name='store'),
    path('checkout/', checkout_view, name='checkout')
)
