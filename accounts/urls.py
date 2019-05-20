from django.conf.urls import url
from django.urls import include
from accounts import views as auth_views

urlpatterns = [
    url('login/', auth_views.user_login, name='login'),
    url('logout/', auth_views.user_logout, name='logout'),
    url('signup/',auth_views.signup, name='signup'),                         
]