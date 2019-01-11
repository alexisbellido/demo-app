from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from django.http import HttpResponseRedirect

from .models import Article, TVProgram
from .forms import TVProgramForm


def article_total_count(request):
    count_articles = Article.objects.count()
    return HttpResponse("There are {0:d} articles".format(count_articles))


def add_tv_program(request):
    """
    Make sure there are not conflicting TV programs at the provided time.
    """
    if request.method == 'POST':
        form = TVProgramForm(request.POST)
        if form.is_valid():
            tv_program = form.save()
            # return HttpResponseRedirect('/demo/tv-program-added')
            return tv_program.get_absolute_url()

    else:
        form = TVProgramForm()

    return render(
        request,
        'demo/add-tv-program-form.html',
        {'form': form}
    )

def tv_program_added(request):
    return render(request, 'demo/tv-program-added.html')


def detail(request, tv_program_id):
    tv_program = get_object_or_404(TVProgram, pk=tv_program_id)
    return render(request, 'demo/detail.html', {'tv_program': tv_program})
