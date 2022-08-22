from django.shortcuts import render, HttpResponse
from .models import Category, Dish, Event


def base(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    special = Dish.objects.filter(special=True)
    event = Event.objects.filter()

    data = {'categories': categories,
            'dishes': dishes,
            'specials': special,
            'events': event
            }

    return render(request, 'base.html', context=data)
