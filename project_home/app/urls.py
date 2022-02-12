from django.urls import path

from .views import *
app_name ='app'
urlpatterns=[
    path('', home_view, name='home'),
    path('login', login_view, name='login'),
]