from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
import logging
# Create your views here.


from django.http import HttpResponse

# Game page
def index(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("Email")
            password = request.POST.get("Password")
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                logging.info("Login success: user=%s" % username)
                return HttpResponseRedirect('/game/')
            else:
                return render(request, 'home.html', {'login': "false"})
        except:
            logging.info("Error! Received HTTP POST method, but data is wrong.")
            return HttpResponse("Error! Received HTTP POST method, but data is wrong.")
    else:
        logging.info("Error! Expecting  POST method!")
        return HttpResponse("Error! Expecting POST method!")


def logout(request):
        if request.method == 'POST':
            auth.logout(request)
            return HttpResponseRedirect('/game/')
        else:
            logging.info("Error! Expecting  POST method!")
            return HttpResponse("Error! Expecting POST method!")


def memory(request):
    return render(request, 'memory.html')

def game_2048(request):
    return render(request, 'game_2048.html')