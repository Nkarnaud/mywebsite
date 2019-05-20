from django.http import HttpResponse
from .models import Category
from django.shortcuts import render, get_object_or_404

# Create your views here.
def blog_home(request):
    cat = Category.objects.all()
    return render(request, 'blog_home.html', {'cat': cat})

def about(request):
    # do something...
    return render(request, 'about.html')

def category_articles(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    return render(request, 'articles.html', {'cat': cat})
 

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})