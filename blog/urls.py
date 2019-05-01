from django.conf.urls import url
from blog import views as blog_view

urlpatterns = [
     url(r'^$', blog_view.home, name='home'),
]