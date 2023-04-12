from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import UserModel
from board.models import board
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/home')
    else:
        return redirect('/signin')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/signin')
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'signin.html')

def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return  redirect('/')
        else:
            return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)

        if password != password2:
            return render(request, 'signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password, email=email)
            return redirect('/signin')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def my_page(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    board_list = board.objects.all().filter(user_id=id)
    if me.id == id:
        show_my_board = True
    else:
        show_my_board = False
    return render(request, 'my_page.html', {'click_user': click_user,'board_list': board_list, 'show_my_board': show_my_board})



@login_required
def view_users(request):
    if request.method == 'GET':
        me = request.user
        all_user = UserModel.objects.all().exclude(id=me.id)
    return render(request, 'home.html', {'all_user': all_user})



