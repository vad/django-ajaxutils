"""
syntactic sugar for Ajax requests in django
"""

from decorator import decorator

from django.http import Http404

from .http import JsonResponse


def ajax(login_required=False, require_GET=False, require_POST=False,
         require=None):
    """
    Usage:

    @ajax(login_required=True)
    def my_ajax_view(request):
        return {'count': 42}
    """

    def ajax(f, request, *args, **kwargs):
        """ wrapper function """
        if login_required:
            if not request.user.is_authenticated():
                return JsonResponse({
                    'status': 'error',
                    'error': 'Unauthorized',
                    }, status=401)

        # check request method
        method = None
        if require_GET:
            method = "GET"
        if require_POST:
            method = "POST"
        if require:
            method = require
        if method and method != request.method:
            return JsonResponse({
                'status': 'error',
                'error': 'Method not allowed',
                }, status=405)

        try:
            response = f(request, *args, **kwargs)
        except Http404:
            return JsonResponse({
                'status': 'error',
                'error': 'Not found',
            }, status=404)

        # check if it is an instance of HttpResponse
        if hasattr(response, 'status_code'):
            status_code = response.status_code
            if status_code > 399:
                return JsonResponse({
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

    return decorator(ajax)
