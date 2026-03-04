from django.shortcuts import render
from .models import Portfolio
def index(request):
    save_model = Portfolio.objects.all()
    return render(request, 'index.html', {"save_model":save_model})


def order_form(request):
    return render(request, 'order-form.html')