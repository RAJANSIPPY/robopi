from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from .forms import loginsform

# Create your views here.

def home_view(request,*args, **kwargs):
    return render(request, "app/home.html", {})

def login_view(request):
    l_form = loginsform()
    if request.method == "POST":
        l_form = loginsform(request.POST)
        if l_form.is_valid():
            data = l_form.cleaned_data
            user = auth.authenticate(username = data['username'], password = data['passwd'])
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('app:home')
            else:
                l_form.add_error('username', "incorrect details")
                
    context = {
        "form": l_form
    }
    return render(request, "app/login.html",context)

def main_view(request):
    if request.user.is_authenticated:
        return render(request, "app/home.html",{})
    else:
        return login_view(request)
