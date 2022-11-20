from django.urls import path, include

from ecommerce.accounts.views import SignUpView, SignInView, SignOutView, UserDetailsView, UserEditView, UserDeleteView, \
    cart_view

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('cart/', cart_view, name='cart'),
    path('profile/<int:pk>/', include([
        path('', (UserDetailsView.as_view()), name='details user'),
        path('edit/', (UserEditView.as_view()), name='edit user'),
        path('delete/', (UserDeleteView.as_view()), name='delete user'),

    ]))
)
