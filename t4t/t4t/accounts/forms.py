from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': auth_forms.UsernameField}


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)
        field_classes = {
            'username': auth_forms.UsernameField,
        }

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     user.first_name = 'John'
    #     user.last_name = 'Doe'
    #
    #     if commit:
    #         user.save()
    #     return user
