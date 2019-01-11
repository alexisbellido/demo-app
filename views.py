from datetime import time

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, TVProgram

def article_total_count(request):
    count_articles = Article.objects.count()

def add_tv_program(request):
    """
    TODO
    Use form view.
    Make sure there are not conflicting TV programs at the provided time.
    Round seconds to 0 for start time and to 59 for end time as the form only takes
    hour and minute.
    """
    start_time = time(12, 10, 0)
    end_time = time(12, 10, 59)
    count_conflicting_programs = TVProgram.objects.filter(start_time__gte=start_time, end_time__lte=end_time).count()
    return HttpResponse("There are {0:d} TV programs conflicting with that time.".format(count_conflicting_programs))

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
