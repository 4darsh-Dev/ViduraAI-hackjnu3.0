from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

# Create your views here.


def ask_vidura(request):


    return JsonResponse({'name': 'vidura', 'age': 20})

