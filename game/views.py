from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.


from django.http import HttpResponse

# Game page
def index(request):
    return render(request, "base.html")