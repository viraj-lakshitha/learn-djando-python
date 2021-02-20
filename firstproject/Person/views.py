from django.shortcuts import render
from .models import Person

# Create your views here.
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
        'object' : obj
    }
    return render(request, "Person/person.html", context)