from django.shortcuts import render

# Create your views here.

def User(request):
    return render(request, 'user-profile.html')