from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from post.models import Post
from django.contrib.auth import authenticate, login as loginsession
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# from .models import Photo
# from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")

def main(request):
    if request.method == "GET":
        is_user = request.user.is_authenticated
        if is_user == None:  # 현재 접속자가 없는 경우
            return redirect("users:signin")
        else:  # 현재 접속자가 있는 경우
            user1 = request.user  # 현재 접속자
            post_object_list = Post.objects.filter(user=user1.id).last()  # post 테이블에 있는 접속자의 최근 사진 한장
            
            return render(request, "main.html", context=dict(user=user1, posts=post_object_list))


def signup(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signup.html')
    elif request.method == "POST":
        fullname = request.POST.get('fullname','')
        email = request.POST.get('email','')
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        passwordcheck=request.POST.get('passwordcheck','')
        print(password, passwordcheck, username, email, fullname)
        if password != passwordcheck:
            return render(request, 'signup.html',{'error':'패스워드가 틀립니다 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'signup.html', {'error':'아이디와 비밀번호를 입력 해 주세요.'})
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'signup.html', {'error':'아이디가 중복입니다!'})
            else:
                User.objects.create_user(username=username, password=password, fullname=fullname, email=email)
                return redirect('users:signin')


def login(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signin.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('users:main')
        else:
            return render(request, 'signin.html', {'error':'유저이름 혹은 패스워드를 확인해 주세요.'})  # 로그인 실패


@login_required
def logout(request):
    user = request.user.is_authenticated
    if user:
        auth.logout(request)
        return redirect('users:index')
    else:
        return render(request, 'index.html')