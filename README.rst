    .. image:: http://www.mylittledjango.com/media/pony_parts/pony.png
       :alt: AJAX requests for Ponies™
       :align: right

How many times you found yourself writing some views in Django to handle an AJAX request? And how many times you just copy-pasted a view written for synchronous requests and edited them to return a JSON object? And so, how many times you forgot that that ``@login_required`` will actually redirect the request to the login page in case of anonymous users? If this happened to you as many times as it happened to us, you may be start considering using django-ajaxutils.

Django-ajaxutils allows you to define a view as an AJAX view that will return a JSON object and that will handle correctly errors such as user not authenticated and invalid requests. Everything through a simple decorator!

Installation
============

Come on, you know how to do it. (soon on PyPi!)

Usage
=====

If you want to define a view for handling an AJAX request, you have just to decorate it with ``@ajax`` and return a dictionary representing the object to be returned as JSON. If you lack of imagination, check this out::

    @ajax()
    def check_for_some_task(request):
        exit_status = get_status_of_some_task()
        if exit_status is None:
            return {
                'status': 'pending'
            }
    
        return {
            'status': 'completed',
            'exit_status': exit_status
        } 


Requiring authentication
------------------------

If your view requires the user to be authenticated, just write it::

    @ajax(login_required=True)
    def some_very_private_view(request):
        data = perform_something_private()
        return {
            'data': data
        }


In case of an unauthenticated request, a ``401: Unauthorized`` response containing the following JSON object will be returned::

    {
        'status': 'error',
        'error': 'Unauthorized',
    }


Requiring GET / POST
--------------------

``@ajax`` also allows you a quick way to require a particular method for requesting the view. For example, if your view will edit some server-side data, you may accept only POST requests. With ``@ajax`` this is as easy as remembering the first two decimal digits of PI (which are ``1`` and ``4``, btw)::

    @ajax(login_required=True, require_POST=True)
    def submit_my_data(request):
        new_obj = save_my_data()
        return {
            'id': new_obj.pk
        }

This will return a ``405: Method not allowed`` response with the following JSON object in case of illegal requests::

    {
        'status': 'error',
        'error': 'Method not allowed',
    }

You can of course set ``require_GET=True`` for GET requests.