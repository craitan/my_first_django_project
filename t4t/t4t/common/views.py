from django.shortcuts import render
from django.views import generic as views
from t4t.items.models import Item


class HomePageView(views.TemplateView):
    template_name = 'common/home-page.html'


class MarketView(views.ListView):
    model = Item
    template_name = 'common/market-page.html'
