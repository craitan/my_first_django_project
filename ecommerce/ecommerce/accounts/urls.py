from django.urls import path

from ecommerce.accounts.views import SignUpView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='register user'),
)
