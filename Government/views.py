from django.shortcuts import render

# Create your views here.

def Government(request):
    return render(request, 'government-profile.html'),