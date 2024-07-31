from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def Home(request):
    # return (request, "index.html")
    return render(request,"index.html")

def Meeting(request):
    return render(request,"meetings.html")

def Mdetail(request):
    return render(request,"meeting-details.html")

def login(request):
    return render(request,"login.html")