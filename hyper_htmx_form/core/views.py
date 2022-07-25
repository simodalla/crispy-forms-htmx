# import time

from django.http import JsonResponse
from django.shortcuts import render

from .forms import EventUserForm
from .models import Event, EventUser


def index(request):
    event, _ = Event.objects.get_or_create(name="Primavera Sound", number_of_places=3)
    if request.method == "POST":
        # time.sleep(1)
        form = EventUserForm(request.POST, event=event)
        if form.is_valid():
            username = form.cleaned_data["name"]
            EventUser.objects.create(name=username, event=event)
            context = {"users": event.users.all()}
            return render(request, "partials/userlist.html", context)
        context = {"form": form}
        response = render(request, "partials/form.html", context)
        response["HX-Retarget"] = "#submit-form"
        return response
    context = {
        "event": event,
        "form": EventUserForm(),
        "users": event.users.all(),
    }
    return render(request, "index.html", context)


def check_spaces(request):
    event = Event.objects.first()
    spaces_available = event.users.count() < event.number_of_places
    return JsonResponse({"available": spaces_available})
