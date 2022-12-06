from django.core import exceptions


def validate_letters(value):
    min_letters = 3
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters and digits are allowed')

    if len(value) < min_letters:
        raise exceptions.ValidationError('Must have at least three letters.')


def username_validator(value):
    min_letters = 3
    found_letters = 0
    for ch in value:
        if not ch.isalnum() and ch not in ['_', '-']:
            raise exceptions.ValidationError('Username must consist of letters, numbers, underscores and dashes only.')
        elif ch.isalpha():
            found_letters += 1

    if len(value) < min_letters:
        raise exceptions.ValidationError('Username must have at least three letters.')
