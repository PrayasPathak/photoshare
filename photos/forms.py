from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Photo


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter username"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm password"}
        )


class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "description"]
        widgets = {
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 5, "columns": 40}
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
