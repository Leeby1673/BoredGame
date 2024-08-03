from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


# 登入功能
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect("posts/")

    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
