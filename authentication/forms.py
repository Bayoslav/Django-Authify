from django import forms
from .models import User


class RegForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={}))
    password = forms.CharField(
        required=True, min_length=8, widget=forms.PasswordInput(attrs={}))

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", "password")


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={}))
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={}))

    class Meta:

        fields = ("username", "password")
