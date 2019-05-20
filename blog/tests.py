from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, category_articles
from .models import Category

# Create your tests here.

class HomeViewTest(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/blog/')
        self.assertEquals(view.func, home)
    
    def test_home_view_contains_link_to_article_page(self):
        category_articles_url = reverse('category_articles', kwargs={'pk': self.cat.pk})
        self.assertContains(self.response, 'href="{0}"'.format(category_articles_url))

class CategoryViewTest(TestCase):
    def setUp(self):
        Category.objects.create(name="web development", description="Tutorials on web development")
    
    def test_cat_article_view_status(self):
        url = reverse('category_articles', kwargs={'pk': 1})
        response =self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_cat_article_view_not_found_status_code(self):
        url = reverse('category_articles', kwargs={'pk': 99})
        response =self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_cat_article_resolve_view(self):
        view = resolve('/blog/category/1/')
        self.assertEquals(view.func, category_articles)
   
    def test_category_articles_view_contains_link_back_to_homepage(self):
        category_articles_url = reverse('category_articles', kwargs={'pk': 1})
        response = self.client.get(category_articles_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
