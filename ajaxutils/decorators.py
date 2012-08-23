"""
syntactic sugar for Ajax requests in django
"""
from functools import wraps
import warnings

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
                 require_POST=False, require=None, methods=None):

        self.login_required = login_required

        # check request method
        method = None
        if require_GET:
            methods = ["GET"]
        if require_POST:
            methods = ["POST"]
        if require:
            warnings.warn(
                "'require' argument will be removed. Use 'methods' instead",
                PendingDeprecationWarning,
            )
            methods = [require.upper()]
        if methods:
            methods = [method.upper() for method in methods]
        self.methods = methods

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

            if self.methods and request.method not in self.methods:
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
