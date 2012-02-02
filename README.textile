!http://www.mylittledjango.com/media/pony_parts/pony.png(AJAX requests for Ponies™)!

How many times you found yourself writing some views in Django to handle an AJAX request? And how many times you just copy-pasted a view written for synchronous requests and edited them to return a JSON object? And so, how many times you forgot that that <code>@login_required</code> will actually redirect the request to the login page in case of anonymous users? If this happened to you as many times as it happened to us, you may be start considering using django-ajaxutils.

Django-ajaxutils allows you to define a view as an AJAX view that will return a JSON object and that will handle correctly errors such as user not authenticated and invalid requests. Everything through a simple decorator!

h2. Installation

Come on, you know how to do it. (soon on PyPi!)

h2. Usage

If you want to define a view for handling an AJAX request, you have just to decorate it with <code>@ajax</code> and return a dictionary representing the object to be returned as JSON. If you lack of imagination, check this out:

<pre><code lang="python">@ajax()
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
</code></pre>


h3. Requiring authentication

If your view requires the user to be authenticated, just write it!

<pre><code>@ajax(login_required=True)
def some_very_private_view(request):
    data = perform_something_private()
    return {
        'data': data
    }
</code></pre>

In case of an unauthenticated request, a <code>401: Unauthorized</code> response containing the following JSON object will be returned:

<pre><code>{
    'status': 'error',
    'error': 'Unauthorized',
}</code></pre>

h3. Requiring GET / POST

<code>@ajax</code> also allows you a quick way to require a particular method for requesting the view. For example, if your view will edit some server-side data, you may accept only POST requests. With <code>@ajax</code> this is as easy as remembering the first two decimal digits of PI (which are "14", btw):

<pre><code>@ajax(login_required=True, require_POST=True)
def submit_my_data(request):
    new_obj = save_my_data()
    return {
        'id': new_obj.pk
    }
</code></pre>

This will return a <code>405: Method not allowed</code> response with the following JSON object in case of illegal requests:

<pre><code>{
    'status': 'error',
    'error': 'Method not allowed',
}</code></pre>

You can of course set <code>require_GET=True</code> for GET requests.