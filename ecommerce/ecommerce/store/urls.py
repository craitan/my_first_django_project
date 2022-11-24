from django.urls import path, include

from ecommerce.store.views import store_view, checkout_view, details_product, edit_product, delete_product, add_product

urlpatterns = (
    path('', store_view, name='store'),
    path('checkout/', checkout_view, name='checkout'),
    path('add/', add_product, name='add product'),
    path('item/<int:pk>/', include([
        path('', details_product, name='details product'),
        path('edit/', edit_product, name='edit product'),
        path('delete/', delete_product, name='delete product'),

    ])),
)
