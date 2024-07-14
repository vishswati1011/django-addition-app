How to start with Django web 
Create basic Addition app 


## 1. Brew install python
2. brew install pip3
3. pip3 —version 
4. python3 —version
5. pip3 install Django
6. Check Django version
	python3 -m django —version

## 7. Create Django project

## Move desktop and python folder
$ : django-admin startproject jobprotal 


## 8. Run djandgo project
	Move inside folder then run cmd
	$: python3 manage.py runserver


## 9. Create app

	In terminal write cmd to create app
	$: python manage.py startapp guestapp

## 10. Add app name into installed_apps in main project folder in setting.py

## 11. Include the guest app url into job portal url.py file
Example:
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('guest', include('guestapp.urls')),
    path('admin/', admin.site.urls),
]

## 12. Create a urls.py file in guest app and add a blank path for guest
Example
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
] 

## 13. Create function for quest page in views .py
	from django.shortcuts import render
	from django.http import HttpResponse

### Create your views here.
 	def index(request):
    		return HttpResponse("Hello, world. You're at the guestapp index.")


## 14. Add path in urls.py for add 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/add',views.addition,name='addition'),
] 


## 15. Create a function for addition in view.py

def addition (request):
    a=100
    b=400
    c=a+b
    return HttpResponse('The sum is:'+str(c))

## 16. Now check on bowser 
	localhost:8000/guest
	localhost:8000/guest/add

## 17. Write an html code for addition file 
	first create a template folder in guest app folder then create a guest app folder in template folder 
Then create addition.html file

### additon.html

<!DOCTYPE html>
<html lang="en">
<head>
   <title>Addition</title>
</head>
<body>
    
    <form action="guest/add" method="GET">
        <input type="text" name="num1" placeholder="Enter first number">
        <br/>
        <input type="text" name="num2" placeholder="Enter second number">
        <br/>
        <input type="submit" value="Add" name="btn_submit">
    </form>
</body>
</html>


Now change views.py file to render addition.html on browser and also change addition function to dynamic addition

### views.py

from django.shortcuts import render
from django.http import HttpResponse

### Create your views here.

def index(request):
    return render(request, 'guestapp/addition.html')

def addition(request):
    a=int(request.GET['num1'])
    b=int(request.GET['num2'])
    c=a+b
    return HttpResponse('The sum is:'+str(c))









