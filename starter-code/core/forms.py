from datetime import datetime

from crispy_forms.helper import FormHelper
from django import forms


class UniversityForm(forms.Form):

    SUBJECT_CHOICES = (
        (1, "Web Dev"),
        (2, "Cyber"),
        (3, "Dev Ops"),
    )

    name = forms.CharField()
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
