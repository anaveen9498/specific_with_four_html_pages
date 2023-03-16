from django.shortcuts import render

# Create your views here.


def third(request):
    return render(request,'third.html')


def fourth(request):
    return render(request,'fourth.html')