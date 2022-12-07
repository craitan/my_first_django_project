from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ecommerce.core.form_mixins import RemoveLabelsMixin, AddPlaceholdersMixin

UserModel = get_user_model()


class UserEditForm(RemoveLabelsMixin, AddPlaceholdersMixin,auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('password',)
        field_classes = {'username': auth_forms.UsernameField}


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
