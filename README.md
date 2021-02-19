# Learn Django Framework using Python

----

#### Writing First Django Application (For Windows)

##### Install Virtual ENV & Djanog and Create brand new project

----

* Create virtual environment inside the project folder `virtualenv -p python3 venv`
* To activate the virtual environment `venv\Scripts\activate`
* Install Django `pip install django==2.0.7`
* To deactivate the virtual environment `deactivate`
* Create first django project `django-admin startproject <name-of-the-project> .`
* Run project on Localhost `python manage.py runserver`, normally redirected to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

##### Configurations and Super User

----

* To sync and activate whatever configuration in django project `cd src` --> `python manage.py migrate`
* View Django administration [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
* Create super user to login django administration `python manage.py createsuperuser` , before create super user make super to activate the virtual enviroment

##### Create new Application( Components )

----

* To create components or application `python manage.py <name-of-the-component>
* When you do changes in model.py file then make sure to run the commands `python manage.py makemigrations` and `python manage.py migrate`
