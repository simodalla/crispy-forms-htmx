from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

from crispy_forms.utils import render_crispy_form

from .forms import UniversityForm


# Create your views here.
def index(request):
    if request.method == "GET":
        context = {"form": UniversityForm()}
        return render(request, "index.html", context)

    form = UniversityForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        template = render(request, "profile.html", context={})
        template["Hx-Push"] = "/profile/"
        return template

    context = {}
    context.update(csrf(request))
    form_html = render_crispy_form(form, context=context)
    return HttpResponse(form_html)
