from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Authenticate.models import userdetails
from itertools import chain
from  django . shortcuts  import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Farmer.models import  Followers, LikePost, Post, Profile
from django.db.models import Q
from django.urls import reverse
# Create your views here.

def homepage(request):
    following_users = Followers.objects.filter(follower=request.user.username).values_list('user', flat=True)
    
    # Fetch posts by the logged-in user and the users they follow
    post = Post.objects.filter(Q(user=request.user.username) | Q(user__in=following_users)).order_by('-created_at')

    # Fetch the profile of the logged-in user
    profile = Profile.objects.get(user=request.user)

    context = {
        'post': post,
        'profile': profile,
    }
    return render(request, 'User/user-profile.html',context)



# Create your views here.

def weatherr(request):
    return render(request, 'User/weather.html')

def jobb(request):
    return render(request, 'User/job.html')

def markett(request):
    return render(request, 'User/market.html')

def policies(request):
    return render(request, 'Government/policies.html')

def profilee(request):
    return render(request, 'User/profile2.html')

@login_required(login_url='login')
def user_logout(request):
    user_logout(request)
    return redirect('login')

    

@login_required(login_url='login')
def uploadd(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='login')
def likess(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id)
    
        like_filter = LikePost.objects.filter(post_id=id, username=username).first()

        if like_filter is None:
            new_like = LikePost.objects.create(post_id=id, username=username)
            post.no_of_likes = post.no_of_likes + 1
        else:
            like_filter.delete()
            post.no_of_likes = post.no_of_likes - 1

        post.save()

        # Generate the URL for the current post's detail page
        print(post.id)

        # Redirect back to the post's detail page
        url = reverse('home_post', args=[id])

        # Redirect back to the post's detail page
        return redirect(url)
    
@login_required(login_url='login') # Ensure that 'Login' matches the actual login URL
def profile_details(request,username):
    user_object = User.objects.get(username=username)
    print(user_object)
    profile = Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=username).order_by('-created_at')
    user_post_length = len(user_posts)

    follower = request.user.username
    user = username
    
    if Followers.objects.filter(follower=follower, user=user).first():
        follow_unfollow = 'Unfollow'
    else:
        follow_unfollow = 'Follow'

    user_followers = len(Followers.objects.filter(user=username))
    user_following = len(Followers.objects.filter(follower=username))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'profile': profile,
        'follow_unfollow':follow_unfollow,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    
    
    if request.user.username == username:
        if request.method == 'POST':
            if request.FILES.get('image') == None:
             image = user_profile.profileimg
             bio = request.POST['bio']
             location = request.POST['location']

             user_profile.profileimg = image
             user_profile.bio = bio
             user_profile.location = location
             user_profile.save()
            if request.FILES.get('image') != None:
             image = request.FILES.get('image')
             bio = request.POST['bio']
             location = request.POST['location']

             user_profile.profileimg = image
             user_profile.bio = bio
             user_profile.location = location
             user_profile.save()
            

            return redirect('/Userprofile/'+username)
        else:
            return render(request, 'User/profile2.html', context)
        
    return render(request, 'User/profile2.html', context)
    

@login_required(login_url='login')
def deletee(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/Userprofile/'+ request.user.username)


@login_required(login_url='login')
def search_resultss(request):
    query = request.GET.get('q')

    users = Profile.objects.filter(user__username__icontains=query)
    posts = Post.objects.filter(caption__icontains=query)

    context = {
        'query': query,
        'users': users,
        'posts': posts,
    }
    return render(request, 'User\search_user.html', context)

@login_required(login_url='login')
def home_postt(request,id):
    post = get_object_or_404(Post, id=id)
    profile = Profile.objects.get(user=request.user)
    context={
        'post':post,
        'profile':profile
    }
    return render(request, 'User/user-profile.html',context)



def followw(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Followers.objects.filter(follower=follower, user=user).first():
            delete_follower = Followers.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/Userprofile/'+user)
        else:
            new_follower = Followers.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/Userprofile/'+user)
    else:
        return redirect('/')