from django.urls import path

from t4t.common.views import MarketView, HomePageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),
    path('market/', MarketView.as_view(), name='market'),

)