Demo Django Application
===========================================

This is a Django application with solutions to some exercises.

It's not packaged as a distributable Python package so simply copy the directory where this README file is into a working Django project and add the following to INSTALLED_APPS:

.. code-block:: bash

  'demo.apps.DemoConfig',

And add the following to your project's URLConf.

.. code-block:: bash

  path('demo/', include('demo.urls')),


Exercise #1
-------------------------------------------------------

Run the following management command.

.. code-block:: bash

  $ django-admin swap_case "Up and Down 1.2" 

See the swap_case method in demo.management.commands.swap_case for details.


Exercise #2
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


Exercise #3
-------------------------------------------------------

Exercise #4
-------------------------------------------------------

Run the following management command.

.. code-block:: bash

  $ django-admin mutate_string "pythom" --position 5 --character n

See the mutate_string method in demo.management.commands.mutate_string for details.