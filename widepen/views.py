from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.shortcuts import render, redirect
from django.db import IntegrityError
from widepen.models import User, Post
from bs4 import BeautifulSoup
from .forms import post_form, profile_edit_form
from django.db.models import Q



def search_post(request):
    if request.method == 'GET':
        search_data = request.GET['search_query']

        results = Post.objects.filter(
            Q (title__icontains=search_data) |
            Q (user__username__icontains=search_data) |
            Q (user__first_name__icontains=search_data) |
            Q (user__last_name__icontains=search_data)
        )

        for post in results:
            if post.story:
                soup = BeautifulSoup(post.story, 'html.parser')
                img_tag = soup.find('img')
                if img_tag and 'src' in img_tag.attrs:
                    post.image_url = img_tag['src']
                else:
                    post.image_url = None

        return render(request, "widepen/search.html",{
            "search_result" : results,
            "search_data" : search_data
        })
    else:
        return redirect("index")
    
        
def post_delete(request, post_id):
    current_post = Post.objects.get(id=post_id)
    current_user = request.user

    if current_post.user == current_user:
        current_post.delete()

        return redirect("index")

    else:
        return HttpResponseForbidden("You are not allowed to delete this post.")


@login_required
def add_to_bookmark(request, post_id):
    current_post = Post.objects.get(id=post_id)
    current_user = request.user
    current_post.bookmark.add(current_user)

    return HttpResponseRedirect(reverse("post_read", args=(post_id, )))

@login_required
def remove_from_bookmark(request, post_id):
    current_post = Post.objects.get(id=post_id)
    current_user = request.user
    current_post.bookmark.remove(current_user)

    return HttpResponseRedirect(reverse("post_read", args=(post_id, )))

def view_bookmark(request):
    current_user = request.user
    posts = current_user.user_bookmark.all()

    for post in posts:
        if post.story:
            soup = BeautifulSoup(post.story, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and 'src' in img_tag.attrs:
                post.image_url = img_tag['src']
            else:
                post.image_url = None

    return render(request, "widepen/bookmark.html", {
        "user_bookmarks": posts
    })


def category(request, category_name):
    posts = Post.objects.filter(category=category_name).order_by('-post_date')

    for post in posts:
        if post.story:
            soup = BeautifulSoup(post.story, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and 'src' in img_tag.attrs:
                post.image_url = img_tag['src']
            else:
                post.image_url = None  # Set a default value if no image found

    return render(request, "widepen/index.html",{
        "category_post": posts
    })

        


def index(request):
    # Fetch posts and extract image URLs
    posts = Post.objects.order_by('-post_date').all()
    
    for post in posts:
        if post.story:
            soup = BeautifulSoup(post.story, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and 'src' in img_tag.attrs:
                post.image_url = img_tag['src']
            else:
                post.image_url = None  # Set a default value if no image found

    return render(request, 'widepen/index.html', {
        'posts': posts,
        
        })


def post_read(request, post_id):
    post = Post.objects.get(id=post_id)
    post_in_bookmark = request.user in post.bookmark.all()
    return render(request, "widepen/post_read.html", {
        "user_post" : post,
        "post_in_bookmark": post_in_bookmark
    })


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user).order_by('-post_date')

    for post in posts:
        if post.story:
            soup = BeautifulSoup(post.story, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and 'src' in img_tag.attrs:
                post.image_url = img_tag['src']
            else:
                post.image_url = None  # Set a default value if no image found


    return render(request, "widepen/profile.html", {
        "user_profile": user,
        "user_post": posts
    })   


def edit_profile(request, user_id):
    # Fetch the user instance
    user = User.objects.get(id=user_id)

    if request.user != user:
        return render(request, "widepen/error.html",{
            "message": "Unauthorized Access"
        })

    if request.method == "POST":
        form = profile_edit_form(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Save the form associated with the user instance
            form.save()
            return redirect('profile', user_id=user.id)  # Redirect to the profile page after saving
    else:
        form = profile_edit_form(instance=user)  # Populate the form with user data

    # Render the form
    return render(request, 'widepen/profile_edit.html', {
        'form': form,
        })



def publish_edit(request, post_id):
    current_post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = post_form(request.POST, request.FILES, instance=current_post)
        if form.is_valid():
            form.save()
            return redirect('post_read', post_id=current_post.id)
        
    else:
        form = post_form(instance=current_post)
        return render(request, 'widepen/publish_edit.html',{
             'form': form,
             'current_post': current_post
            })



@login_required
def publish(request):
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)  # Include request.FILES for file uploads
        print(request.POST)
        if form.is_valid():
            print("fine 1")
            new_post = form.save(commit=False)  # Get the unsaved instance of the model
            new_post.user = request.user  # Assuming user is stored in the session
            new_post.save()
            print("fine 2") 
            return redirect ('post_read', post_id=new_post.id)  # Replace 'index' with your desired URL name
    else:
        form = post_form() 
        
    return render(request, 'widepen/user_writes.html', {
        'form': form
        })

    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "widepen/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "widepen/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "widepen/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username,
                email,
                password, 
                first_name=firstname, 
                last_name=lastname
                )
            user.save()
        except IntegrityError:
            return render(request, "widepen/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "widepen/register.html")
