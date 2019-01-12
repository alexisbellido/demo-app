from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .models import Article, TVProgram
from .forms import TVProgramForm


def article_total_count(request):
    count_articles = Article.objects.count()
    return HttpResponse("There are {0:d} articles".format(count_articles))


def add_tv_program(request):
    """
    Assumes the same TV programs are running every day so it only checks
    for conflicting times during one day.

    Uses a minimal function-based view instead of a class-based view inheriting from
    django.views.generic.edit.FormView for demonstration purposes.
    """
    if request.method == 'POST':
        form = TVProgramForm(request.POST)
        if form.is_valid():
            tv_program = form.save()
            return redirect(tv_program)
    else:
        form = TVProgramForm()

    return render(
        request,
        'demo/add-tv-program-form.html',
        {'form': form}
    )


def detail(request, tv_program_id):
    tv_program = get_object_or_404(TVProgram, pk=tv_program_id)
    context = {
        'tv_program': tv_program
    }
    return render(request, 'demo/detail.html', context)
