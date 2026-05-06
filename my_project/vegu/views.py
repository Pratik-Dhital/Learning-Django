from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def receipe(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        receipe_image = request.FILES.get("receipe_image")
        description = data.get('description')
        
        Recipe.objects.create(
            name = name,
            description = description,
            receipe_image = receipe_image
        ) 
        return redirect('/receipe/')
    queryset = Recipe.objects.all()
    context = {"receipe" : queryset}
    return render(request, "receipe.html", context)