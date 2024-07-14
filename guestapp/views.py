from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method=="POST":
        a=int(request.POST["num1"])
        b=int(request.POST["num2"])
        c=a+b
        return render(request,"guestapp/addition.html",{'key1':a,'key2':b,'key': 'addition is'+str(c)})    
    else:    
        return render(request, 'guestapp/addition.html')


