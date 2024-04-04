from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import AddPostForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm

def homePage(request):
    posts = Post.objects.all().order_by('-postDate')[:3]
    return render(request, "home.html", {
        'posts': posts
    })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "user/post-detail.html", {
        'post': post
    })

def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = AddPostForm()

    return render(request, "user/add-post.html", {
        'form': form
    })

def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("homePage")
    return render(request, "user/delete-post.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = AddPostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("postDetail", pk=post.pk)
    else:
        form = AddPostForm()

    return render(request, "user/edit-post.html", {
        'post': post,
        'form': form
    })

def sign_up_page(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")

    else:
        form = NewUserForm()

    context = {'form': form}

    return render(request, "./sign-up.html", context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homePage")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, "./login.html", context)

def logout_request(request):
    logout(request)
    return redirect("homePage")