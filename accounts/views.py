from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from .models import AuthUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm


# Create your views here.
#signup views
def signup(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if AuthUser.objects.filter(username=form.cleaned_data['username']).exists():
                context = {'form': form,'error_message':'Username already exists.'}
                return render(request, 'registration/signup.html', context)
            elif AuthUser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, 'registration/signup.html', {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, 'registration/signup.html', {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                #objects = UserManager()
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.last_login = datetime.now()
                user.is_staff =0
                user.is_active =0 
                user.date_joined=datetime.now()
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to dashbord page:
                return render(request, 'dashboard.html')

   # No post data availabe.
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html', {'form': form})

#login view
def user_login(request):
    #creating a form isntance with data from frquest
    if request.method == 'POST':
        form= LoginForm(request.POST)
        # check if form is valide
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request, 'dashboard.html')
                else:
                    return render(request, 'registration/login.html', {
                        'form': form,
                        'error_message': 'Your account is inactive.'
                    })
            else:
                return render(request, 'registration/login.html',
                {'form': form,
                'error_message': 'Incorrect username and / or password.'} )
    else:
        form = LoginForm()
    return render(request,'registration/login.html', {'form': form})

#logout view
@login_required
def user_logout(request):
    logout(request)
    return render(request,'registration/login.html', {'form':form})
