from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def article_total_count(request):
    count_articles = Article.objects.count()
    return HttpResponse("There are {0:d} articles".format(count_articles))

def detail(request, question_id):
    context = {
        'question_id': question_id,
        'person': {
            'name': 'mike',
            'quote': 'all dogs like to play'
        },
        'colors': ['red', 'green', 'blue']
    }
    return render(request, 'demo/detail.html', context)
