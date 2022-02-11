from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1 style='color:blue;font-size:46px;'>Hello World!</H1>")
    # return render(request, "home.html", {})