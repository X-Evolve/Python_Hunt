from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        cpassword = request.POST['cpasswd']
        error_message = []
        
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                error_message.append("Username already taken, Please try a different one!")
                return render(request,'accounts/signup.html',{'errors': error_message})

            try:
                # Use Django's validate_password to check password complexity
                validate_password(password)
            
                user = User.objects.create_user(username=username, password = password)
                auth.login(request,user)
                return redirect('home')
            except ValidationError as e:
                error_message = list(e)
            
            return render(request,'accounts/signup.html',{'errors': error_message})
            
        else:
            error_message.append("Passwords must match!")
            return render(request,'accounts/signup.html',{'errors':error_message})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            return render(request,'accounts/login.html',{'error':"Your username or password is incorrect!"})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
