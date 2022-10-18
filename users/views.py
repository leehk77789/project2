from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login as loginsession
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, "index.html")

def main(request):
    if request.method == "GET":
        is_user = request.user.is_authenticated
        if is_user == None:
            return redirect("users:signin")
        else:
            return render(request, "main.html")

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        passwordcheck=request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)
            return HttpResponse("가입완료")
        else:
            return("signup.html")
    else:
        return HttpResponse("허용되지 않은 메소드입니다.") 

def login(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('users:main')
        else:
            return HttpResponse("로그인 실패")