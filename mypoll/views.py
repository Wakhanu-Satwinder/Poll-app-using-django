from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

'''from django.models import Choice, Question'''

def polls(request):
    '''return HttpResponse("Hello world")'''
    return HttpResponse('polls/')
