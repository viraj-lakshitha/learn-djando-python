from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Home Page !</h1>")  # string of HTML code
    # Creating simple dictionary to render data to frontend
    data = {
        "name": "Viraj",
        "uni": "IIT",
        "subjects" : ["CSP","OOP","Algo"],
        "code" : [10,20,30]
    }
    return render(request, "home.html", data)


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page !</h1>")
