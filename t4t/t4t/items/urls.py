from django.urls import path, include

from t4t.items.views import add_item, details_item, edit_item, delete_item

urlpatterns = (
    path('add/', add_item, name='add item'),

    path('<str:username>/item/<int:pk>/', include([
        path('', details_item, name='details item'),
        path('edit/', edit_item, name='edit item'),
        path('delete/', delete_item, name='delete item'),
    ]))
)
