from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#categories
class Category(models.Model):
    name = models.CharField(max_length = 25, unique=True)
    description = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

#Articles 
class Article(models.Model):
    Titel = models.CharField(max_length = 500)
    messages = models.TextField()
    last_updated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='articles')
    created_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='articles')

#comments
class Comment(models.Model):
    comments_content = models.TextField(max_length = 500)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comments")
    comment_author = models.CharField(max_length = 50)
    comment_date = models.DateTimeField(null=True)
    comment_created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comments')
    comment_update_date = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name='+')
    