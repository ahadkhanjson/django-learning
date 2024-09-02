from django.http import HttpResponse 
from django.shortcuts import render 



def home(request):
    # return HttpResponse(" You are at Home . ")
    return render(request,'index.html')

def about(request):
    return HttpResponse("You are at About")

def contact(request):
    return HttpResponse("You are at Contact")