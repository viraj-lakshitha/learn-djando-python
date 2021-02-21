from django.shortcuts import render
from .models import Person
from .forms import PersonForm


# Create your views here.
def person_create_view(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonForm()
    context = {
        'form': form
    }
    return render(request, "Person/person_create.html", context)


def person_detail_view(request):
    obj = Person.objects.get(id=1)

    # Method 1
    # context = {
    #     "firstName" : obj.firstName,
    #     "lastName" : obj.lastName,
    #     "emailAddress" : obj.emailAddress,
    # }

    # Method 2
    context = {
        'object': obj
    }
    return render(request, "Person/person_details.html", context)
