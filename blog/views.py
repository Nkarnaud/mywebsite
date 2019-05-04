from django.http import HttpResponse
from .models import Category
from django.shortcuts import render

# Create your views here.
def home(request):
    cat = Category.objects.all()
    return render(request, 'home.html', {'cat': cat})

def about(request):
    # do something...
    return render(request, 'about.html')

def category_articles(request):
    # do something...
    return render(request, 'category_articles.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})