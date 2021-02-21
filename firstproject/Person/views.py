from django.shortcuts import render
from .models import Person
from .forms import PersonForm,RawPersonForm


from .forms import PersonForm


# Create your views here.

### Method 1
# def person_create_view(request):
#     form = PersonForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = PersonForm()
#     context = {
#         'form': form
#     }
#     return render(request, "Person/person_create.html", context)

### Method 2
def person_create_view(request):

    my_form = RawPersonForm(request.POST)
    context = {
        "form" : my_form
    }

    if my_form.is_valid():
        print(my_form.cleaned_data)
    else:
        print(my_form.errors)

    return render(request, "Person/person_create.html", context)

def person_search_view(request):
    search_keyword = request.POST.get('title')
    context = {'keyword': search_keyword}
    return render(request, "Person/person_search.html", context)


    context = {}
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
