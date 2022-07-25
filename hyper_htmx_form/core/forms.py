from django import forms


class EventUserForm(forms.Form):
    name = forms.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        if "event" in kwargs:
            self.event = kwargs.pop("event")
        super().__init__(*args, **kwargs)

    def clean(self):
        # print("***", self.event.users.count())
        if self.event.users.count() >= self.event.number_of_places:
            # print("-----")
            raise forms.ValidationError("No spaces at this event")
        return super().clean()
