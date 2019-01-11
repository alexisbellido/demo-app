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

Exercise #3
-------------------------------------------------------

Exercise #4
-------------------------------------------------------

Run the following management command.

.. code-block:: bash

  $ django-admin mutate_string "pythom" --position 5 --character n

See the mutate_string method in demo.management.commands.mutate_string for details.