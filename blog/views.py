from django.http import HttpResponse
from .models import Category
from django.shortcuts import render

# Create your views here.
def home(request):
    cat = Category.objects.all()
    return render(request, 'home.html', {'cat': cat})