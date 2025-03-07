from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', login_page, name='login'),
    path('check_login', check_login, name='check login'),
    path('logout', logout_func, name='logout'),
    path('reg_func', reg_func, name='register user'),
    path('reg', register, name='register page'),
]