from django.urls import path

from t4t.common.views import index

urlpatterns = (
    path('', index, name='index'),
)