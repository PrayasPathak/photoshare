from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("", views.gallery, name="gallery"),
    path("photo/<str:pk>/", views.viewPhoto, name="photo"),
    path("add/", views.addPhoto, name="add"),
    path("update/<str:pk>/", views.updatePhoto, name="update"),
    path("delete/<str:pk>/", views.deletePhoto, name="delete"),
]
