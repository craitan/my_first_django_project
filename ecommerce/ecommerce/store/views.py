from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ecommerce.store.forms import ShippingAddressForm
from ecommerce.store.models import Product, Cart, CartItem

UserModel = get_user_model()


def store_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store-page.html', context)

@login_required
def checkout_view(request):
    cart, create = Cart.objects.get_or_create(customer=request.user, complete=False)
    items = cart.cartitem_set.all()

    if request.method == 'GET':
        form = ShippingAddressForm()
    else:
        form = ShippingAddressForm()
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.customer = request.user
            shipping.order = cart
            shipping.save()
            return redirect('store')


    context = {

        'items': items,
        'order': cart,
        'form': form,
    }
    return render(request, 'store/checkout-page.html', context)


def item_details_view(request, pk):
    items = Product.objects.get(pk=pk)
    context = {
        'items': items,
    }
    return render(request, 'store/item-details-page.html', context)
