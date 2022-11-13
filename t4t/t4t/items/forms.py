from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from t4t.items.models import Item

UserModel = get_user_model()


class ItemBaseForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'slug' )


class ItemCrateForm(ItemBaseForm):
    pass


class ItemEditForm(ItemBaseForm):
    pass


class ItemDeleteForm(ItemBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
