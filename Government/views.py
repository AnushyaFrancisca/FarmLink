from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def Government(request):
    return render(request, 'Government/government-profile.html')

def post(request):
    return render(request, 'Government/post.html')

def policies(request):
    return render(request, 'Government/policies.html')

def logout_view(request):
    logout(request)
    return redirect('login')

