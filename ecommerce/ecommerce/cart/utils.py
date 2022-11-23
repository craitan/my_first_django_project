from ecommerce.store.models import Cart


def get_user(username):
    return Cart.objects.filter(user__username=username).get()