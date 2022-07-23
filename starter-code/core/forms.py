from datetime import datetime

from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import User


class UniversityForm(forms.ModelForm):
    subject = forms.ChoiceField(choices=User.Subjects.choices)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "max": datetime.now().date,
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "password", "date_of_birth", "subject")
        widgets = {"password": forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_action = reverse_lazy("index")
        # self.helper.form_method = "POST"
        form_id = "university-form"
        self.helper.form_id = form_id
        self.helper.attrs = {
            "hx-post": reverse_lazy("index"),
            "hx-target": f"#{form_id}",
            "hx-swap": "outerHTML",
        }
        self.helper.add_input(Submit("submit", "Submit"))

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) <= 3:
            raise forms.ValidationError("Username is too short")
        return username
