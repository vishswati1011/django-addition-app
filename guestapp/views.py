from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the guestapp index.")

def index(request):
    return render(request, 'guestapp/addition.html')

# def addition (request):
#     a=100
#     b=400
#     c=a+b
#     return HttpResponse('The sum is:'+str(c))

def addition(request):
    a=int(request.GET['num1'])
    b=int(request.GET['num2'])
    c=a+b
    return HttpResponse('The sum is:'+str(c))


