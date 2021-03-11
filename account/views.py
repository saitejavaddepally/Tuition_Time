from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = user_name,password = password1, email = email , first_name = first_name , last_name = last_name)
                user.save()
                print('user created!!')
        else: 
            print("password not matching")
        return redirect('/')
    else:
        return render(request,'registration.html')

def login(request):
    return render(request, 'login.html')