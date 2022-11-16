from django import forms

from t4t.chat.models import Room


class ChatCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('user',)
