from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # user meta to add more data beyond default fields
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'street', 'city', 'state', 'zip_code', 'phone', 'age')


class CustomUserChangeForm(UserChangeForm):
    # user meta to add more data beyond default fields
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'street', 'city', 'state', 'zip_code', 'phone', 'age')
