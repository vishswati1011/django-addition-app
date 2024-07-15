from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'helloapp/index.html')
def about(request):
    return render(request, 'helloapp/about.html')
def contact(request):
    return render(request, 'helloapp/contact.html')
# def addition(request):   
