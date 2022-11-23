from django.contrib.auth import get_user_model
from django.shortcuts import render

from ecommerce.store.models import Product, Cart, CartItem

UserModel = get_user_model()


def store_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store-page.html', context)


def checkout_view(request):
    cart, create = Cart.objects.get_or_create(customer=request.user, complete=False)
    items = cart.cartitem_set.all()

    context = {
        'items': items,
        'order': cart
    }
    return render(request, 'store/checkout-page.html', context)


def item_details_view(request, pk):
    items = Product.objects.get(pk=pk)
    context = {
        'items': items,
    }
    return render(request, 'store/item-details-page.html', context)
