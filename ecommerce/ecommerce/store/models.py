from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from ecommerce.core.validators import validate_letters

UserModel = get_user_model()


class Product(models.Model):
    MAX_LEN_PRODUCT_NAME = 100
    MIN_LEN_PRODUCT_NAME = 2

    product_name = models.CharField(
        max_length=MAX_LEN_PRODUCT_NAME,
        unique=True,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(
                MIN_LEN_PRODUCT_NAME,
            ),
        ),
    )

    product_price = models.FloatField(
        validators=(
            validators.MinValueValidator(1),
        ),
        null=False,
        blank=False,
    )

    product_image = cloudinary_models.CloudinaryField(
        null=False,
        blank=False,
    )

    product_description = models.TextField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    customer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    order_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    complete = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    def get_cart_total(self):
        order_products = self.cartitem_set.all()
        total = sum([item.get_total_price() for item in order_products])

        return total

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    quantity = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True
    )

    date_added = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.product.product_name

    def get_total_price(self):
        total = self.product.product_price * self.quantity
        return total


class ShippingInfo(models.Model):
    ADDRESS_MAX_LEN = 100
    ZIP_CODE_LEN = 4
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 20

    customer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
        null=False,
        blank=False,
    )

    city = models.CharField(
        max_length=ADDRESS_MAX_LEN,
        null=False,
        blank=False,
    )

    zipcode = models.CharField(
        max_length=ZIP_CODE_LEN,
        null=False,
        blank=False,
    )

    date_added = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters,
        ),
        null=False,
        blank=False,
    )


class ContactUs(models.Model):
    MAX_SUBJECT_LENGTH = 20
    MIN_SUBJECT_LENGTH = 2
    MIN_LEN_MESSAGE = 10
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 20

    date_added = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    subject = models.CharField(
        max_length=MAX_SUBJECT_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_SUBJECT_LENGTH),
            validate_letters,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    massage = models.TextField(
        max_length=250,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MESSAGE),
        ),
        null=False,
        blank=False,
    )

    massage_checked = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
