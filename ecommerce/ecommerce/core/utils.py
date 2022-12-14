from django.shortcuts import get_object_or_404

from ecommerce.store.models import Product, Cart, CartItem


def get_item(pk):
    return get_object_or_404(Product, pk=pk)


def get_cart(customer):
    return Cart.objects.filter(customer=customer, complete=False).get()


def get_or_create_cart(customer):
    return Cart.objects.get_or_create(customer=customer, complete=False)


def get_or_create_cart_item(cart, item):
    return CartItem.objects.get_or_create(product=item, cart=cart)


def get_total_items_count(items):
    return sum([item.quantity for item in items])


def get_total_items_price(items):
    return sum([item.get_total_price() for item in items])
