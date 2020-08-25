from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = "abcdefghijklmnoprstuwxyz"
    upper = characters.upper()
    numbers = "1234567890"
    specials = "!@#$%^&*()"

    length = int(request.GET.get("length"))

    if request.GET.get("upper"):
        characters += upper

    if request.GET.get("numbers"):
        characters += numbers

    if request.GET.get("specials"):
        characters += specials

    myPassword = ""

    for _ in range(length):
        myPassword += random.choice(list(characters))

    return render(request, 'generator/generatedPassword.html', {'password': myPassword})

def about(request):
    return render(request,'generator/about.html')
