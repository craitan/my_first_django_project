from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from ecommerce.core.utils import get_item, get_or_create_cart, get_total_items_count, get_total_items_price
from ecommerce.store.forms import ShippingAddressForm, ProductCrateForm, ProductEditForm, ProductDeleteForm
from ecommerce.store.models import Product

UserModel = get_user_model()


def store_view(request):
    products = Product.objects.order_by('product_name').all()
    page = Paginator(products, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page
    }
    return render(request, 'store/store-page.html', context)


# TODO: Have to get second opinion for the search bar
def search_bar_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(product_name__icontains=searched)
        page = Paginator(products, 6)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)

        context = {
            'searched': searched,
            'page': page
        }
        return render(request, 'store/search-bar-result.html', context)


@staff_member_required
def add_product(request):
    if request.method == 'GET':
        form = ProductCrateForm()
    else:
        form = ProductCrateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('store')

    context = {
        'form': form,
    }

    return render(request, 'store/product-add-page.html', context)


@staff_member_required
def edit_product(request, pk):
    item = get_item(pk)

    if request.method == 'GET':
        form = ProductEditForm(instance=item)
    else:
        form = ProductEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('details product', pk=pk)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'store/product-edit-page.html', context)


@staff_member_required
def delete_product(request, pk):
    item = get_item(pk)

    if request.method == 'GET':
        form = ProductDeleteForm(instance=item)
    else:
        form = ProductDeleteForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('store')

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'store/product-delete-page.html', context)


@login_required
def details_product(request, pk):
    item = get_item(pk)
    context = {
        'items': item,
    }
    return render(request, 'store/product-details-page.html', context)


@login_required
def checkout_view(request):
    cart, create = get_or_create_cart(request.user)
    items = cart.cartitem_set.order_by('product').all()
    items_count = get_total_items_count(items)
    items_price = get_total_items_price(items)

    if request.method == 'GET':
        form = ShippingAddressForm()
    else:
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.customer = request.user
            shipping.order = cart
            cart.complete = True
            cart.save()
            shipping.save()

            return redirect('store')

    context = {

        'items': items,
        'order': cart,
        'form': form,
        'items_count': items_count,
        'items_price': items_price,
    }
    return render(request, 'store/checkout-page.html', context)
