from django.urls import path

from ecommerce.store.views import store_view, checkout_view, item_details_view

urlpatterns = (
    path('', store_view, name='store'),
    path('checkout/', checkout_view, name='checkout'),
    path('item/<int:pk>/', item_details_view, name='item details'),
)
