from django.shortcuts import render

# App level imports
from .models import Category, Photo


# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {
        "categories": categories,
        "photos": photos,
    }
    return render(request, "photos/gallery.html", context)


def addPhoto(request):
    return render(request, "photos/add_photo.html")


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {"photo": photo}
    return render(request, "photos/photo.html", context)
