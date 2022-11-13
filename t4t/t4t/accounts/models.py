from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from t4t.core.model_mixin import ChoicesEnumMixin
from t4t.core.validators import validate_letters_and_numbers


class Region(ChoicesEnumMixin, Enum):
    europe = 'Europe'
    asia_pacific = 'Asia/Pacific'
    north_america = 'North America'


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
    )

    region = models.CharField(
        choices=Region.choices(),
        max_length=Region.max_len(),

    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_region(self):
        return f'{self.get_region_display()}'
