from django.shortcuts import render

# Create your views here.

def Government(request):
    return render(request, 'Government/government-profile.html')