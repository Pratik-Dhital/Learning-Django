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

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
       

    context = {"receipe" : queryset}
    return render(request, "receipe.html", context)

def update_receipe(request, id):
    receipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        receipe.name = request.POST.get('name')
        receipe.description = request.POST.get('description')
        if request.FILES.get('receipe_image'):
            receipe.receipe_image = request.FILES.get('receipe_image')
        receipe.save()
        return redirect('/receipe/')
    context = {'receipe': receipe}
    return render(request, 'update_receipe.ht ml', context)

def delete_receipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')