from django.shortcuts import render

# Create your views here.

def home_sub_url(request):
    return render(request, 'sub_url.html')
