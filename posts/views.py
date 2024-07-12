from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(
        request,
        "post.html",
    )


def newPost(request):
    return render(
        request,
        "newPost",
    )
