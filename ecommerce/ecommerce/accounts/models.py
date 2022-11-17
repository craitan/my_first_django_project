from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from ecommerce.accounts.validators import validate_letters_and_numbers


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 20

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters_and_numbers,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters_and_numbers,
        )
    )


    email = models.EmailField(
        unique=True,
        null=True,
        blank=False,
    )