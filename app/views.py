from django.shortcuts import render, redirect
from app.models import Post
from app.forms import SubscribeForm, NewUserForm

from django.contrib.auth import login

# Create your views here.

def register_user(request):
    form = NewUserForm()
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("/")

    context = {"form":form}
    return render(request, "registration/registration.html", context)

def index(request):
    posts = Post.objects.all()
    subscribe_form = SubscribeForm()
    subscribe_successful=None

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            request.session['subscribed'] = True
            subscribe_successful = 'Subscribed Successful'
            subscribe_form = SubscribeForm()
    context = {"posts":posts, 'subscribe_form':subscribe_form, 'subscribed_successful':subscribe_successful}
    return render(request, 'app/index.html', context)

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    
    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count+1
    post.save()
    context = {"post":post}
    return render(request, 'app/post.html', context)