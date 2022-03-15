from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# to show what users received from server
# 새로운 page 작성하려면 여기 밑에다 새 request 붙여 넣으면 됨.
def index(request):
    return render(request, "hello/index.html")


def kang(request):
    return HttpResponse("Hello, kang!")


def han(request):
    return HttpResponse("Hello, han!")

# render(req, "html", {context})
def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })
