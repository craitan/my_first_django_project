from django import forms

from ecommerce.store.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('date_added', 'order', 'customer')