from crispy_forms.utils import render_crispy_form
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

from .forms import UniversityForm


# Create your views here.
def index(request):
    if request.method == "GET":
        context = {"form": UniversityForm()}
        return render(request, "index.html", context)

    form = UniversityForm(request.POST)
    if form.is_valid():
        user = form.save()
        return HttpResponse("Hi")

    # https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html#ajax-validation-recipe
    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return HttpResponse(form_html)
