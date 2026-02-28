from django.shortcuts import render

def index(request):

    return render(request, 'index.html')


def order_form(request):
    pass