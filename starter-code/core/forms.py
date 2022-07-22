from datetime import datetime

from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UniversityForm(forms.Form):

    SUBJECT_CHOICES = (
        (1, "Web Dev"),
        (2, "Cyber"),
        (3, "Dev Ops"),
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "hx-get": reverse_lazy("index"),
                "hx-trigger": "keyup",
            }
        )
    )
    age = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "max": datetime.now().date,
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy("index")
        self.helper.form_method = "GET"
        self.helper.add_input(Submit("submit", "Submit"))
