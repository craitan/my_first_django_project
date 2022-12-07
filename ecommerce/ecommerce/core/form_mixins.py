class DisabledFormMixin:
    disabled_attrs_name = 'readonly'
    disabled_fields = ()
    fields = {}

    def _disabled_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['readonly'] = 'readonly'


class RemoveLabelsMixin:
    fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class AddPlaceholdersMixin:
    fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key not in ['password', 'password1', 'password2']:
                field.widget.attrs['placeholder'] = key.capitalize().replace('_', ' ')
