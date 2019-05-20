from django.conf.urls import url
from blog import views as blog_view

urlpatterns = [
     url(r'^$', blog_view.blog_home, name='blog_home'),
     url(r'^about/$', blog_view.about, name='about'),
     url(r'^category/(?P<pk>\d+)/$', blog_view.category_articles, name='category_articles'),
     url(r'^about/company/$', blog_view.about_company, name='about_company'),
]