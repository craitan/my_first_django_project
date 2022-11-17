
from django.shortcuts import render
from django.views import generic as views




class StoreView(views.TemplateView):
    template_name = 'store/store-page.html'
    extra_context = {}


class CartView(views.TemplateView):
    template_name = 'store/cart-page.html'
    extra_context = {}


class CheckoutView(views.TemplateView):
    template_name = 'store/checkout-page.html'
    extra_context = {}
