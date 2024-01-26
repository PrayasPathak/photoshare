from django.shortcuts import render


# Create your views here.
def gallery(request):
    return render(request, "photos/gallery.html")


def addPhoto(request):
    return render(request, "photos/add_photo.html")


def viewPhoto(request, pk):
    return render(request, "photos/photo.html")