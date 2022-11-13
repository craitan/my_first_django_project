from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('t4t.common.urls')),
    path('accounts/', include('t4t.accounts.urls')),
    path('items/', include('t4t.items.urls')),
    path('chat/', include('t4t.chat.urls')),
]
