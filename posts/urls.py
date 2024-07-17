from django.urls import path
from . import views

urlpatterns = {
    path("", views.index),
    path("newpost", views.newPost, name="new_post"),
}
