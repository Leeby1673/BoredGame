from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# 登入功能
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("posts")

    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


# 登出功能
@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("login")
