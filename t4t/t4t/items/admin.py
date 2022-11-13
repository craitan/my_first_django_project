from django.contrib import admin

from t4t.items.models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
