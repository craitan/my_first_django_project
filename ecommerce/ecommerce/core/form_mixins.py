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
                field.widget.attrs[self.disabled_attrs_name] = self.disabled_attrs_name
