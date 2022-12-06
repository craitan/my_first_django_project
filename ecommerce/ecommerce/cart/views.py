from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ecommerce.core.utils import get_item, get_or_create_cart, get_or_create_cart_item, get_cart, get_total_items_count, \
    get_total_items_price



@login_required
def new_cart_view(request):
    cart, create = get_or_create_cart(request.user)
    items = cart.cartitem_set.order_by('product').all()
    items_count = get_total_items_count(items)
    total_price = get_total_items_price(items)
    context = {
        'items': items,
        'cart': cart,
        'count': items_count,
        'total_price': total_price,
    }

    return render(request, 'cart/new-cart-page.html', context)


@login_required
def add_to_cart(request, pk):
    cart, create = get_or_create_cart(request.user)
    item = get_item(pk)
    cart_item, created = get_or_create_cart_item(cart=cart, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('new cart')


def remove_from_cart(request, pk):
    cart = get_cart(request.user)
    item = get_item(pk)
    cart_item, created = get_or_create_cart_item(cart=cart, item=item)

    if not created:
        cart_item.quantity -= 1
        cart_item.save()
        if cart_item.quantity == 0:
            cart_item.delete()

    return redirect('new cart')
