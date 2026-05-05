from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def receipe(request):
    return render(request, "receipe.html")