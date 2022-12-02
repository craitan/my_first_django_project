from django import forms

from ecommerce.core.form_mixins import DisabledFormMixin
from ecommerce.store.models import ShippingAddress, Product, ContactUs


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCrateForm(ProductBaseForm):
    pass


class ProductEditForm(ProductBaseForm):
    pass


class ProductDeleteForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('product_name', 'product_price', 'product_description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('date_added', 'order', 'customer')


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('massage_checked',)
