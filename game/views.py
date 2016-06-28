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
    return render(request, "base.html")

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("Email")
            password = request.POST.get("Password")
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # Correct password, and the user is marked "active"
                auth.login(request, user)
                logging.info("Login success: user=%s, keepin=%s" % (username, keep_login))
                return HttpResponseRedirect('/game/')
            else:
                # Return login failure flag
                data = {"login": "failure"}
                json_response = json.dumps(data)
                logging.info("Login failure: user=%s" % username)
                return HttpResponse(json_response, content_type='application/json')
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