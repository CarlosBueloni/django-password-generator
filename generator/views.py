from django.shortcuts import render
import random
import string
# Create your views here.
def index(request):
    return render(request, 'generator/index.html')

def password(request):
    characters = list(string.ascii_lowercase)

    length = 10

    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})