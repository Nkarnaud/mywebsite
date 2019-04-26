from django.db import models

# Create your models here.

#categories

class category(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 300)

#Articles 
class Article(models.Model):
    categories = models.ManyToManyField(category, blank=True)
    name = models.CharField(max_length = 255)
    description = models.TextField()

#comments

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length = 50)
    comment_content = models.CharField(max_length = 200)
    comment_date = models.DateTimeField(auto_now_add=True)