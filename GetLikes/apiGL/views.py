from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(
        '<!DOCTYPE html > <head> <metacharset = "UTF-8"> <title> Главная страница </title> </head> <body> <h1> Главная страница </h1> <br> <p><a href = "https://oauth.vk.com/authorize?client_id=51822829&redirect_uri=https://localhost&scope=12&display=popup"> Ссылка </p> </body> </html>'
    )
