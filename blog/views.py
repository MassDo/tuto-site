from django.shortcuts import render
from .models import Article

# Create your views here.
def home_page(request):
    return render(request, 'blog/base.html')

def prerequisites(request):
    return render(request, 'blog/prerequisites.html')

def article_detail(request, article_id):
    return render(request, f'blog/articles/{article_id}.html')