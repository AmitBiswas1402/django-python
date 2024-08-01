from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hellow from Home")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hellow from about")

def contact(request):
    return HttpResponse("Hellow from contact")