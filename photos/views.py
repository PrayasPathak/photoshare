from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# App level imports
from .models import Category, Photo
from .forms import CustomUserCreationForm
import PIL


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("gallery")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("gallery")
    page = "login"
    return render(request, "photos/login_register.html", context={"page": page})


def logout_user(request):
    logout(request)
    return redirect("login")


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("gallery")
    context = {"form": form, "page": page}
    return render(request, "photos/login_register.html", context)


@login_required(login_url="login")
def gallery(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    category = request.GET.get("category")
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(category__name=category, category__user=user)
    context = {
        "categories": categories,
        "photos": photos,
    }
    return render(request, "photos/gallery.html", context)


@login_required(login_url="login")
def addPhoto(request):
    user = request.user
    categories = user.category_set.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES["image"]
        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                user=user, name=data["category_new"]
            )
        else:
            category = None

        # Creating an image
        try:
            Photo.objects.create(
                category=category, description=data["description"], image=image
            )
            messages.success(request, "Photo was added successfully.")
            return redirect("gallery")
        except PIL.UnidentifiedImageError:
            messages(
                request,
                "An error occurred while adding the image. Please make sure the image is not corrupt.",
            )
            return redirect("add")
    context = {"categories": categories}
    return render(request, "photos/add_photo.html", context)


@login_required(login_url="login")
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {"photo": photo}
    return render(request, "photos/photo.html", context)
