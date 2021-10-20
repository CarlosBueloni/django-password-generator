from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'generator/index.html')

def password(request):
    return render(request, 'generator/password.html')