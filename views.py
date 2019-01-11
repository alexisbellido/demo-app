from django.shortcuts import render


def index(request):
    return render(request, 'demo/index.html')


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
