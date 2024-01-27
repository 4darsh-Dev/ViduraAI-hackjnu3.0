from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def vidura(reuqest):
    return render(reuqest, 'vidura.html')


