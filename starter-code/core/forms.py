from datetime import datetime

from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import User


class UniversityForm(forms.ModelForm):
    subject = forms.ChoiceField(
        choices=User.Subjects.choices,
        widget=forms.Select(
            attrs={
                "hx-get": reverse_lazy("check-subject"),
                "hx-trigger": "change",
                "hx-target": "#div_id_subject",
            }
        ),
    )
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
        widgets = {
            "password": forms.PasswordInput(),
            "username": forms.TextInput(
                attrs={
                    "hx-get": reverse_lazy("check-username"),
                    "hx-trigger": "keyup changed",
                    "hx-target": "#div_id_username",
                }
            ),
        }

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

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if User.objects.filter(subject=subject).count() >= 3:
            raise forms.ValidationError("There are no spaces on this course")
        return subject
