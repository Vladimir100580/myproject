from django.shortcuts import render, redirect
from .models import User, Order
from datetime import date, timedelta


def users(request):
    users = User.objects.all()
    return render(request, 'gb_app3/users.html', {'users': users})


def user_products(request, user_id, days=0):
    str_d = 'последние ' + str(days) + ' дней'
    orders = Order.objects.filter(customer=user_id).order_by('-date_ordered')
    if days == 0:
        str_d = 'всё время'
    else:
        orders = orders.filter(date_ordered__gte=date.today() - timedelta(days=days))
    user = User.objects.get(pk=user_id)
    return render(request, 'gb_app3/products_list.html', {'orders': orders, 'user': user, 'days': str_d})


def index(request):
    return render(request, 'gb_app3/index.html')

