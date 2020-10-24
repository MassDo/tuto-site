from django.db import models

# Create your models here.
class Article(models.Model):
    """
        Les articles sont dans le dossier ./redaction_articles.
        Il sont de base en md puis convertis en html.
        La portion style et texte est alors enregistré dans deux champs différents,
        pour etre utilisés dans les templates de façons s'éparée.

        article.md => article.html => implémentation de la BDD.
    """ 
    titre = models.CharField(max_length=50)
    style = models.TextField()
    texte = models.TextField()