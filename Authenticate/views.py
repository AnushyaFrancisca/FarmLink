from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

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