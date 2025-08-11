from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the home page of the demo application!")
    return render(request, 'index.html')
def about(request):
    return HttpResponse("This is the about page of the demo application!")