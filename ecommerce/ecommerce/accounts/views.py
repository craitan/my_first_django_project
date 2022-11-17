from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from ecommerce.accounts.forms import UserCreateForm


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('store')