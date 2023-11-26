from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home.html", context)

def register_view(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username__iexact = username).exists():
            error = "Username Is Already Taken!"

        elif len(password) < 8:
            error = "Password Must Atleast Be 8 Character Long!"

        else:
            user = User.objects.create(username=username, password=make_password(password))
            login(request, user)

    context = {"error": error}
    return render(request, "register.html", context)

def login_view(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username__iexact = username).exists():
            error = "User With Username Doesn't Exist!"

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            error = "An Error Occured During Login! There Maybe A Problem With Your Credentials!"

    context = {"error": error}
    return render(request, "login.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")

def learn_view(request):
    context = {}
    return render(request, "learn.html", context)

def quizzes_view(request):
    context = {}
    return render(request, "quizzes.html", context)

def add_word_view(request):
    context = {}
    return render(request, "add_word.html", context)

def my_progress_view(request):
    context = {}
    return render(request, "my_progress.html", context)

def settings_view(request):
    context = {}
    return render(request, "settings.html", context)
