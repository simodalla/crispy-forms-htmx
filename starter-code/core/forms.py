from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse_lazy

from .models import User


class UniversityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_action = reverse_lazy("index")
        # self.helper.form_method = "POST"
        self.helper.form_id = "university-form"
        self.helper.attrs = {
            "hx-post": reverse_lazy("index"),
            "hx-target": f"#{self.helper.form_id}",
            "hx-swap": "outerHTML",
        }
        self.helper.add_input(Submit("submit", "Submit"))

    SUBJECT_CHOICES = (
        (1, "Web Development"),
        (2, "Systems Programming"),
        (3, "Data Science"),
    )

    subject = forms.ChoiceField(choices=User.Subjects.choices)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "max": datetime.now().date()})
    )

    class Meta:
        model = User
        fields = ("username", "password", "date_of_birth", "subject")
        widgets = {"password": forms.PasswordInput}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_username(self):
        print(self.cleaned_data)
        username = self.cleaned_data["username"]
        if len(username) <= 3:
            raise forms.ValidationError("Username is too short")
        return username
