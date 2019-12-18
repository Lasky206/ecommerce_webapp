from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .templates.forms import ContactForm, LoginForm, RegisterForm


def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home page.'
    }
    print('---------------')
    print(request.user.is_authenticated)
    print('---------------')
    if request.user.is_authenticated is True:
        context["premium_content"] = "YEEEAAAAHHHH"
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'Welcome to the about page'
    }
    return render(request, 'about.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the contact page',
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
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, "login.html", context)


User = get_user_model()


def register_req(request):
    form = RegisterForm(request.POST or None)
    context = {
        'title': 'Login',
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "register.html", context)
