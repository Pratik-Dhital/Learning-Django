from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_fun(request):
    peoples = [
        {'name' : 'Pratik', 'age' : 22},
        {'name' : 'Jagerna', 'age' : 21},
        {'name' : 'Likhil', 'age' : 23},
        {'name' : 'Dennis', 'age' : 24},
        {'name' : 'Ashutosh', 'age' : 25},
    ]

    vegetables = ['alu', 'golveda', 'kakro', 'karela']

    text = """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat, rerum. Incidunt vel debitis consequatur inventore sed iure quae eius, provident repellendus nisi consectetur ex facere maiores dolor impedit laborum velit."""

    return render (request, "index.html", context = {'page':'Django Tutorial', 'peoples' : peoples, 'text' : text, 'vegetables' : vegetables})

def second_fun(request):
    return HttpResponse("This is a success message")

def contact(request):
    context = {"page" : "Contact"}
    return render(request, "contact.html", context)

def about_us(request):
    context = {'page' : 'About Us'}
    return render(request, "aboutus.html", context) 