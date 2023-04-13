from django import forms
from user.models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email', 'bio']