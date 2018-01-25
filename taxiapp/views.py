from django.shortcuts import render,redirect
from .forms import UserSignup, UserLogin, UserForm, RestaurantForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def restaurant_home(request):
    return render(request, 'restaurant.html', {})

def restaurant_signup(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password'],
            ))
            return redirect("taxi:restaurant_home")

    context = {
        "user_form": user_form,
        "restaurant_form": restaurant_form,
    }
    return render(request, 'restaurant_signup.html', context)

def restaurant_signin(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()
    context = {
        "user_form": user_form,
        "restaurant_form": restaurant_form,
    }
    return render(request, 'restaurant_signin.html', context)

def restaurant_signout(request):
    logout(request)
    return redirect("taxi:home")

def usersignup(request):
    context = {}
    form = UserSignup()
    context['form'] = form
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password

            user.set_password(password)
            user.save()

            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)

            return redirect("taxi:home")
        messages.error(request, form.errors)
        return redirect("taxi:signup")
    return render(request, 'signup.html', context)

def userlogin(request):
    context = {}
    form = UserLogin()
    context['form'] = form
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('taxi:home')

            messages.error(request, "Wrong username/password combination. Please try again.")
            return redirect("taxi:login")
        messages.error(request, form.errors)
        return redirect("taxi:login")
    return render(request, 'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("taxi:home")
