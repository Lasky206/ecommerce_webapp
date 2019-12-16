from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .templates.forms import ContactForm, LoginForm


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'about.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'form': form
    }
    if form.is_valid():
        pass
    if request.method == "POST":
        print(request.POST)
    return render(request, 'contact.html', context)


def login_req(request):
    form = LoginForm(request.POST or None)
    context = {
        'title': 'Login',
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, "login.html", context)


def register_req(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        pass
    return render(request, "register.html", context)
