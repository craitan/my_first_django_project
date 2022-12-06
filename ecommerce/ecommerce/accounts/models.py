from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from ecommerce.core.validators import validate_letters, username_validator


class AppUser(auth_models.AbstractUser):
    MAX_USERNAME_LENGTH = 20
    MIN_USERNAME_LENGTH = 2
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LENGTH),
            username_validator
        ),
        error_messages={
            'max_length': f'Username must be a maximum of {MAX_USERNAME_LENGTH} characters.',
            'min_length': f'Username must be at least {MIN_USERNAME_LENGTH} characters long.',
        },
        null=False,
        blank=False,
        unique=True,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters,
        ),
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters,
        ),
        blank=True,
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
