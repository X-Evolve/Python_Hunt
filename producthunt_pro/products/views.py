from django.shortcuts import render

# URLS:

urls = {
    'basicpy/': 'Python Basics',
    'installpy/': 'Install Python',
    'aboutpython/': 'About Python',
    'keywords/': 'Keywords',
    'variables/': 'Variables',
    'datatypes/': 'Data Types',
    'sets/': 'Sets',
    'statements/': 'Statements',
    'tuples/': 'Tuples',
    'string/': 'Strings',
    'lists/': 'Lists',
    'dicts/': 'Dictionaries',
    'PythonLoops/':'Loops'
}
context = {
    'urls' : urls
}
# Create your views here.
def home(request):
    return render(request,'products/home.html', context)

def basicpy(request):
    return render(request,'products/index.html', context)

def installpy(request):
    return render(request,'products/installation.html', context)

def aboutpython(request):
    return render(request, 'products/Python_Intro.html', context)

def keywords(request):
    return render(request, 'products/Keywords.html', context)

def datatypes(request):
    return render(request, 'products/python_data_types.html', context)
  
def statements(request):
    return render(request, 'products/statements.html', context)
  
def sets(request):
    return render(request, 'products/sets.html', context)

def tuples(request):
    return render(request, 'products/tuples.html', context)

def lists(request):
    return render(request, 'products/lists.html', context)

def string(request):
    return render(request,'products/string.html', context)

def variables(request):
    return render(request,'products/variables.html', context)

def dicts(request):
    return render(request,'products/dictionaries.html', context)

def PythonLoops(request):
    return render(request,'products/PythonLoops.html', context)


