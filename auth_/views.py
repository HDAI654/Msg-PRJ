from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_page(request):
    return render(request, 'login.html', context={"form":forms.flogin}) 
    
def check_login(request):
    form = forms.flogin(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            res = HttpResponseRedirect("/panel")
            res.set_cookie('username', str(username))
            return res
        else:
            return HttpResponseRedirect("login")
    else:
        return HttpResponseRedirect("login")
    
def logout_func(request):
    logout(request)
    return HttpResponseRedirect("login") 
  
def reg_func(request):
    if request.method == 'POST':
        form = forms.freg(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.data["username"]).exists():
                us = User.objects.create_user(email=form.data["email"], password=form.data["password"], username=form.data["username"])
                us.first_name = form.data["name"]
                us.last_name = form.data["family"]
                us.save()
                return HttpResponseRedirect("/panel")
            else:
                return HttpResponse("This Username Already Exists")
        else:
            return HttpResponse("Registration Failed")

def register(request):
    return render(request=request, template_name='Reg.html', context={"form": forms.freg})
    
    