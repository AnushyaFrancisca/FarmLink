from django.shortcuts import render

# Create your views here.

def Admin_interface(request):
    return render(request, 'admin-dashboard.html'),