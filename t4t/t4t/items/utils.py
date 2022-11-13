from t4t.items.models import Item


def get_items(pk, username):
    return Item.objects.filter(user__username=username, pk=pk).get()
