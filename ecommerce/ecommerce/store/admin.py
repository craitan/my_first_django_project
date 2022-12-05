from django.contrib import admin

from ecommerce.store.models import Product, Cart, CartItem, ShippingInfo, ContactUs


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'complete',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'date_added')


@admin.register(ShippingInfo)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cart', 'date_added')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_added', 'massage_checked')
