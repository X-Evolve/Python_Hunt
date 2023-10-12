from django.shortcuts import render

def python_editor(request):
    return render(request, 'code_editor/editor.html')
