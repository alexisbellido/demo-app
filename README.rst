Demo Django Application
===========================================

This is a Django application with solutions to the proposed exercises.

Installation
-------------------------------------------------------

It's not packaged as a distributable Python package so you install it by simply copying the directory where this README file resides into a working Django project, add the following to INSTALLED_APPS:

.. code-block:: bash

  'demo.apps.DemoConfig',

and add the following line to your project's URLConf:

.. code-block:: bash

  path('demo/', include('demo.urls')),


Solution to Exercise #1
-------------------------------------------------------

Run the following management command.

.. code-block:: bash

  $ django-admin swap_case "Up and Down 1.2" 

See the swap_case method in demo.management.commands.swap_case for details.


Solution to Exercise #2
-------------------------------------------------------

The bug is a TypeError exception because str and int can't be concatenated without a type conversion.

Here's a couple of alternatives for the response.

.. code-block:: bash

  return HttpResponse("There are " + str(count_articles) + " articles")

.. code-block:: bash
  
  return HttpResponse("There are {0:d} articles".format(count_articles))

The performance issue is the article count. The number should come from the count method of the queryset, which uses SELECT COUNT(*), to avoid retrieving all objects.

The corrected view should be like this.

.. code-block:: bash

  from django.http import HttpResponse
  from .models import Article

    def article_total_count(request):
        count_articles = Article.objects.count()
        return HttpResponse("There are {0:d} articles".format(count_articles))


Solution to Exercise #3
-------------------------------------------------------

This is a very simple implementation and just verifies that there's no time overlap between TV Programs and that the end time is always after the start time.

Please review the TVProgram model and the corresponding form at
`models.py <https://github.com/alexisbellido/demo-app/blob/master/models.py>`_ and ` `forms.py <https://github.com/alexisbellido/demo-app/blob/master/forms.py>_.

I'm using a simple form instead of a ModelForm and just raising forms.ValidationError instead of using the Django's messages framework for demonstration purposes.

I also added a simple view to display the form at /add-tv-program and a basic detail view, to which a successful form submission redirects.

Minimal templates and inline style are also included.

Solution to Exercise #4
-------------------------------------------------------

Run the following management command.

.. code-block:: bash

  $ django-admin mutate_string "pythom" --position 5 --character n

See the mutate_string method in demo.management.commands.mutate_string for details.