from django.contrib.auth import get_user_model
from django.shortcuts import render

from ecommerce.store.models import Product, Order, OrderItem

UserModel = get_user_model()


def store_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store-page.html', context)




def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_products': 0}

    context = {
        'items': items,
        'order': order
    }
    return render(request, 'store/checkout-page.html', context)
