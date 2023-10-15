from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'products/home.html')

def basicpy(request):
    return render(request,'products/index.html')

def installpy(request):
    return render(request,'products/installation.html')

def aboutpython(request):
    return render(request, 'products/Python_Intro.html')

def keywords(request):
    return render(request, 'products/Keywords.html')

def datatypes(request):
    return render(request, 'products/python_data_types.html')
  
def statements(request):
    return render(request, 'products/statements.html')
  
def sets(request):
    return render(request, 'products/index.html')

def tuples(request):
    return render(request, 'products/tuples.html')

def lists(request):
    return render(request, 'products/lists.html')

def string(request):
    return render(request,'products/string.html')


