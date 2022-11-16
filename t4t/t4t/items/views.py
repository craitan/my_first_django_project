from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from t4t.core.decorators import is_owner
from t4t.items.forms import ItemCrateForm, ItemEditForm, ItemDeleteForm
from t4t.items.models import Item

from t4t.items.utils import get_items

UserModel = get_user_model()


@login_required
def add_item(request):
    if request.method == 'GET':
        form = ItemCrateForm()
    else:
        form = ItemCrateForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('my items', pk=request.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'items/item-add-page.html', context)


def details_item(request, pk, username):
    items = get_items(pk, username)

    context = {
        'item': items,
        'item_pk': items.pk,
        'username': username,

    }
    return render(request, 'items/item-details-page.html', context)


def edit_item(request, pk, username):
    item = get_items(pk, username)

    # if not is_owner(request, item):
    #     return redirect('details item', username=username, pk=pk)

    if request.method == "GET":
        form = ItemEditForm(instance=item)
    else:
        form = ItemEditForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('details item', username=username, pk=pk)

    context = {
        'form': form,
        'pet_pk': pk,
        'username': username,
    }

    return render(request, 'items/item-edit-page.html', context)


def delete_item(request, pk, username):
    item = get_items(pk, username)

    if request.method == "GET":
        form = ItemDeleteForm(instance=item)
    else:
        form = ItemDeleteForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)
        # TODO: fix the redirect
    context = {
        'form': form,
        'pet_pk': pk,
        'username': username,
    }

    return render(request, 'items/item-delete-page.html', context)



