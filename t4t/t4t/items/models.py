from enum import Enum

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify

from t4t.core.model_mixin import ChoicesEnumMixin

UserModel = get_user_model()


class ArmorPiece(ChoicesEnumMixin, Enum):
    helm = 'Helm'
    armor = 'Armor'
    gloves = 'Gloves'
    boots = 'Boots'
    weapon = 'Weapon'
    shield = 'Shield'

class Item(models.Model):
    MAX_LEN_NAME = 50
    MIN_LEN_NAME = 3
    MIN_ITEM_LEVEL = 1
    MAX_ITEM_LEVEL = 60
    MAX_STATS_ON_ITEM = 200

    item_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(
                MIN_LEN_NAME,
            ),
        ),
    )
    armor_piece = models.CharField(
        choices=ArmorPiece.choices(),
        max_length=ArmorPiece.max_len(),

    )

    item_level = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(
                MIN_ITEM_LEVEL,
            ),
            validators.MaxValueValidator(
                MAX_ITEM_LEVEL,
            ),
        ),
    )

    item_strength = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MaxValueValidator(
                MAX_STATS_ON_ITEM,
            ),
        ),
    )

    item_dexterity = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MaxValueValidator(
                MAX_STATS_ON_ITEM,
            ),
        ),
    )

    item_vitality = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MaxValueValidator(
                MAX_STATS_ON_ITEM,
            ),
        ),
    )

    item_intellect = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MaxValueValidator(
                MAX_STATS_ON_ITEM,
            ),
        ),
    )

    item_short_description = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.item_name}')

        return super().save(*args, **kwargs)

    def get_item(self):
        return f'{self.get_armor_piece_display()}'