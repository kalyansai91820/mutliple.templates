from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(reauest):
    return HttpResponse('hello world')