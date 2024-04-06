from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("", views.gallery, name="gallery"),
    path("photo/<str:pk>/", views.viewPhoto, name="photo"),
    path("add/", views.addPhoto, name="add"),
]
