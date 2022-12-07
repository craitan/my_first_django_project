from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ecommerce.core.form_mixins import RemoveLabelsMixin, AddPlaceholdersMixin

UserModel = get_user_model()


class UserEditForm(RemoveLabelsMixin, AddPlaceholdersMixin, forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }


class UserCreate(RemoveLabelsMixin, AddPlaceholdersMixin, auth_forms.UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
        })
    )

    class Meta:
        model = UserModel
        fields = ('username', 'email',)


class LoginForm(RemoveLabelsMixin, AddPlaceholdersMixin, auth_forms.AuthenticationForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        }))
