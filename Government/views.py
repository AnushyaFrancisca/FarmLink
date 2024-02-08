from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


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


class edit_post(View):
    template_name = 'Government/edit_post.html'
    form_class = BlogPostForm

    def get_object(self, post_id):
        return get_object_or_404(BlogPost, pk=post_id)

    def get(self, request, post_id, *args, **kwargs):
        post = self.get_object(post_id)
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, post_id, *args, **kwargs):
        post = self.get_object(post_id)
        form = self.form_class(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('government-profile')  # Adjust the redirect URL as needed
        else:
            return render(request, self.template_name, {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    # Add logic to handle post deletion
    post.delete()
    return redirect('government-profile')  # Redirect to the government profile page