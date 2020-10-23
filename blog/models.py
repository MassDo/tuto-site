from django.db import models

# Create your models here.
class Article(models.Model):
    """
        Article object for the blog app.
    """ 
    html = models.TextField()