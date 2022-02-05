from django.shortcuts import render
from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html', context={'name': 'kate'})


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)  # Get the wanted category
        pages = Page.objects.filter(category=category)  # Get its associated pages
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:  # Category was not found, don't do anything
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context=context_dict)
