from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Assuming you already have a User model

from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True, default='')
    profileimg = models.ImageField(upload_to='profile_images', default='default.jpg')
    location = models.CharField(max_length=100, blank=True, default='')
    

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='post_images',default='default.jpg')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500,default='')
    username = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username

class Followers(models.Model):
    follower = models.CharField(max_length=100,default=0)
    user = models.CharField(max_length=100,default=0)

    def __str__(self):
        return self.user

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

