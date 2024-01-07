from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField

class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    bio = models.TextField(max_length=150, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default_profile.jpg')

    def __str__(self):
        return self.username
    


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    story = RichTextUploadingField(blank=True, null=True)
    post_date = models.DateTimeField(default=datetime.datetime.now)  
    category = models.TextField(default="sport", blank=False)
    bookmark = models.ManyToManyField(User, blank=True, related_name="user_bookmark")

    def __str__(self):
        return f"Title: {self.title}, Story: {self.story}"
    
    
