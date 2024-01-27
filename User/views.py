from django.shortcuts import render

# Create your views here.

def User(request):
    return render(request, 'User/user-profile.html')