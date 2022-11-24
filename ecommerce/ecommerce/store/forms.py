from django import forms

from ecommerce.store.models import ShippingAddress, Product


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('date_added', 'order', 'customer')


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCrateForm(ProductBaseForm):
    pass


class ProductEditForm(ProductBaseForm):
    pass


class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('product_image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
