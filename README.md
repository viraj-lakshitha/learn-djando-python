# Learn Django Framework using Python 🚩

----

### ⚡ Writing First Django Application (For Windows)

##### 🔥 Install Virtual ENV & Django and Create brand-new project

----

* Create virtual environment inside the project folder `virtualenv -p python3 venv`
* To activate the virtual environment `venv\Scripts\activate`
* Install Django `pip install django==2.0.7`
* To deactivate the virtual environment `deactivate`
* Create first django project `django-admin startproject <name-of-the-project> .`
* Run project on Localhost `python manage.py runserver`, normally redirected to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

##### 🔥 Configurations and Super User

----

* To sync and activate whatever configuration in django project `cd src` --> `python manage.py migrate`
* View Django administration [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
* Create super user to login django administration `python manage.py createsuperuser` , before create super user make super to activate the virtual enviroment

##### 🔥 Create new Application( Components )

----

* To create components or application `python manage.py startapp <name-of-the-component>`
* When you do change in model.py file then make sure to run the commands `python manage.py makemigrations` and `python manage.py migrate`
* Open up Python terminal `python manage.py shell`

##### 🔥 Create new Product Application

----

* To create components or application `python manage.py startapp Products`
* Update the model.py file as
```
from django.db import models
# Create your models here.
class Products(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField()    
```
* Update the admin.py file as
```
from django.contrib import admin

# Register your models here.
from .models import Products

admin.site.register(Products)
```
* In settings.py file update with the component, that you added as `Products` in _INSTALLED_APPS_
* After saving all the files, make migrations as `python manage.py makemigrations` and migrate as `python manage.py migrate`
* Then follow the link -> [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and goto the Product and add products to the database.
* If you want to add the new product to the products, follow these steps 
  (First open python shell as `python manage.py shell`)
```
>> from Products.models import Products
>> Products.objects.all()
>> Products.objects.create(title='New Product', description='Test Description', price='
$ 100', summary='Test from Shell')
```
 For further details about fields [Click](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
 
##### 🔥 Binding with Frontend

----

* First create a new component as PageView `python manage.py startapp PageView` and Update the setting.py file with component.
* Update the view.py file in PageView component as
```
from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Home Page !</h1>")  # string of HTML code

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page !</h1>")
```
* Update the URL of the pages in urls.py file (inside the 'FirstProject' folder) as
```
from django.contrib import admin
from django.urls import path

from PageView import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact')
]
```
