from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def Government(request):
    posts = BlogPost.objects.all()
    return render(request, 'Government/government-profile.html',{'posts':posts})

def post(request):
    return render(request, 'Government/post.html')

def policies(request):
    posts = BlogPost.objects.all()
    return render(request, 'Government/policies.html',{'posts':posts})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('policies')

    return render(request, 'Government/post.html', {'form': form})