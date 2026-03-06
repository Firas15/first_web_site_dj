from django.urls import path
from .views import index, order_form, get_category_portfolio

urlpatterns = [
    path('', index, name='index'),
    path('order_form', order_form, name='order_form'),
    path('get-category-izdeliya/<int:category_id>', get_category_portfolio, name='get_category_izdeliya'),

]
