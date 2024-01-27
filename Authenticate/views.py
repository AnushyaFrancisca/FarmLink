from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # for encryption of password

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from Authenticate.models import userdetails

from builtins import print

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin-dashboard')

            try:
                details = userdetails.objects.get(user_id=user.id)
            except:
                details = None

            if details:

                if details and details.user_type == 'Official':
                    return redirect('government-home')

                elif details and details.user_type == 'Farmer':
                    return redirect('farmer-home')
                
                elif details and details.user_type == 'Others':
                    return redirect('user-home')
            
        else:
            msg = "wrong Credentials"
            return render(request, 'Authenticate/login.html', {'msg': msg})
    return render(request, 'Authenticate/login.html')


def admin_dashboard(request):
    # admin_dashboard.html needs to be added
    return render(request, 'Admin/admin-dashboard.html')


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']  # Add this line
        email = request.POST['email']
        phone = request.POST['phone']
        role = request.POST['role']
        password = request.POST['password']
        
        user = User(
            username=username,  # Include the username parameter
            email=email,
            password=make_password(password),
            first_name=firstName,
            last_name=lastName,
        )
        
        user.save()
        print(f"User created: {user.__dict__}")

        user_details = userdetails(user_id=user.id, user_phone=phone, user_type=role)
        user_details.save()
        print(f"User details created: {user_details.__dict__}")


        return redirect('login')

    return render(request, 'Authenticate/register.html')


def about(request):
    return render(request, 'Authenticate/about.html')


def base(request):
    return render(request, 'Authenticate/base.html')
