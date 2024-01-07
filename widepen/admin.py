from django.contrib import admin

# Register your models here.
from .models import User, Post

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio', 'profile_picture')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'post_date', 'category')




admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
