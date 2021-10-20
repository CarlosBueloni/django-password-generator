from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'generator/index.html', {'password': 'uhfi234##4n$#n1#@%25l#'})