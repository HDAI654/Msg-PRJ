from django.shortcuts import render
from django.http import *
from .forms import * 
from .models import *
import datetime
from django.core import serializers
import json

# Create your views here.

def main_page(request):
    if request.user.is_authenticated:
        form = fmessage()
        return render(request, 'panel.html', {'form': form, 'user_name': request.user.username})
    else:
        return HttpResponseRedirect("/auth/login")
    

# this function run when user click on the send button
def savemessage(request):
    form = fmessage(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print("valid")
            form = fmessage(request.POST)
            new = message(user_id=request.user.id, text=form.data['text'], date_and_time=datetime.datetime.now(), user_name=request.user.username)
            new.save()
            return HttpResponse("true")
        else:
            return HttpResponse("false")
    else:
        return HttpResponse("false")
    


def readmsg(request):
    if request.method == 'POST':
        datalist = message.objects.all()
        myenddata = serializers.serialize('json', datalist)
        return HttpResponse(myenddata)
    else:
        return HttpResponse("false")
