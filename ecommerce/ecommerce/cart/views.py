from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ecommerce.store.models import Cart, Product, CartItem


@login_required
def new_cart_view(request):
    cart, create = Cart.objects.get_or_create(customer=request.user, complete=False)
    items = cart.cartitem_set.all()
    context = {
        'items': items,
        'cart': cart

    }

    return render(request, 'cart/new-cart-page.html', context)


@login_required
def update_cart(request, pk):
    cart = Cart.objects.filter(customer=request.user, complete=False).get()
    item = Product.objects.get(pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=item, cart=cart)



    if not created:
        cart_item.quantity += 1
        cart_item.save(force_update=True, update_fields=['quantity'])



    return redirect('new cart')
