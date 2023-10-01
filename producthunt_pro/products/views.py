from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'products/home.html')

def basicpy(request):
    return render(request,'products/basicpython.html')

def installpy(request):
    return render(request,'products/installation.html')

def aboutpython(request):
    return render(request, 'products/Python_Intro.html')
