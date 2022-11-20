from django.contrib import admin

from ecommerce.store.models import Product, Order, OrderItem, ShippingAddress


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'complete', 'order_transaction',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'zipcode', 'date_added')
