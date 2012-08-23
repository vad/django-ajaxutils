"""
syntactic sugar for Ajax requests in django
"""
from functools import wraps

from django.http import Http404

from .http import JsonResponse


class ajax(object):
    """
    Usage:

    @ajax(login_required=True)
    def my_ajax_view(request):
        return {'count': 42}
    """
    def __init__(self, login_required=False, require_GET=False,
                 require_POST=False, require=None):

        self.login_required = login_required

        # check request method
        method = None
        if require_GET:
            method = "GET"
        if require_POST:
            method = "POST"
        if require:
            method = require
        self.method = method

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(request, *args, **kwargs):
            """ wrapper function """
            if self.login_required:
                if not request.user.is_authenticated():
                    return JsonResponse(
                        {
                            'status': 'error',
                            'error': 'Unauthorized',
                        },
                        status=401
                    )

            if self.method and self.method != request.method:
                return JsonResponse(
                    {
                        'status': 'error',
                        'error': 'Method not allowed',
                    },
                    status=405
                )

            try:
                response = fn(request, *args, **kwargs)
            except Http404:
                return JsonResponse(
                    {
                        'status': 'error',
                        'error': 'Not found',
                    },
                    status=404
                )

            # check if it is an instance of HttpResponse
            if hasattr(response, 'status_code'):
                status_code = response.status_code
                if status_code > 399:
                    return JsonResponse(
                        {
                            'status': 'error',
                            'error': response.content,
                        },
                        status=status_code
                    )

                return response

            status_code = 200
            if isinstance(response, tuple):
                response, status_code = response

            return JsonResponse(response, status=status_code)

        return wrapper
