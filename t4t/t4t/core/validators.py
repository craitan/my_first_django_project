from django.core import exceptions


def validate_letters_and_numbers(value):
    for ch in value:
        if not ch.isalnum():
            raise exceptions.ValidationError('Only letters are allowed')