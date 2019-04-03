from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class FeedbackForm(forms.Form):
    name  =  forms.CharField(max_length=200)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea, required=True,max_length=20000)