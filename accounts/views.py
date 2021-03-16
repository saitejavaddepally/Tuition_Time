from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import user_register_form
from .models import user_register
from validators.account_validator import password_checker
from passlib.hash import pbkdf2_sha256

# Create your views here.

u_r = user_register()


def register(request):
    if request.method == "POST":
        check_username = user_register.objects.filter(
            user_name=request.POST['user_name']).exists()
        if check_username:
            fault_msg = "User Name already taken try another one!!"
            messages.info(request, fault_msg)

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_repeat']

        # password Encryption
        enc_password = pbkdf2_sha256.hash(
            password1, rounds=12000, salt_size=32)
        check_password = password_checker(password2, enc_password)

        # registration

        if check_password and not check_username:
            try:
                user_register_save = user_register.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    user_name=user_name,
                    email=email,
                    password=enc_password
                )

                user_register_save.save()

                return redirect('/dashboard/home')
            except:
                print("Error")
        elif check_password is False:
            fault_msg = "Entered Wrong password"
            messages.info(request, fault_msg)
        else:
            print(form.errors)
    else:
        form = user_register_form()
    return render(request, 'registration.html')




def login(request):
    return render(request, "login.html")
