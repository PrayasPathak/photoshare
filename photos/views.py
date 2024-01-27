from django.shortcuts import render, redirect
from django.contrib import messages

# App level imports
from .models import Category, Photo
import PIL


# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    category = request.GET.get("category")
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    context = {
        "categories": categories,
        "photos": photos,
    }
    return render(request, "photos/gallery.html", context)


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES["image"]
        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                name=data["category_new"]
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


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {"photo": photo}
    return render(request, "photos/photo.html", context)
