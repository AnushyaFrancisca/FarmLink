from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  #for encryption of password

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from Authenticate.models import userdetails


# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('admin-dashboard') #inside redirect write 'admin-dashboard
        else:
            msg = "wrong Credentials"
            return render(request,'Authenticate/login.html',{'msg':msg})
    return render(request,'Authenticate/login.html')

def admin_dashboard(request):
    return render(request,'Admin/admin-dashboard.html') #admin_dashboard.html needs to be added

def register(request):
    if request.method == 'POST':
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        role=request.POST['role']
        password=request.POST['password']
        user=User(first_name=firstName,last_name=lastName,Username=username,Email=email,Phone=phone,Role=role,Password=make_password(password))
        user.save()
        user_details=userdetails(user_id=user.id, user_phone=phone,user_type=role)
        user_details.save()
        return redirect('login')
    return render(request, 'Authenticate/register.html')

def about(request):
    return render(request,'Authenticate/about.html')

def base(request):
    return render(request,'Authenticate/base.html')