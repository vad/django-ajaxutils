"""
syntactic sugar for Ajax requests in django
"""

from decorator import decorator

try:
    import simplejson as json
except ImportError:
    import json

from django.http import HttpResponse


class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` mimetype.
    """
    def __init__(self, data, status=200):
        super(JsonResponse, self).__init__(
            content=json.dumps(data),
            mimetype='application/json', status=status
        )


def ajax(login_required=False, require_GET=False, require_POST=False):
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
        if require_GET:
            if request.method != 'GET':
                return JsonResponse({
                    'status': 'error',
                    'error': 'Method not allowed',
                }, status=405)
        if require_POST:
            if request.method != 'POST':
                return JsonResponse({
                    'status': 'error',
                    'error': 'Method not allowed',
                }, status=405)

        response = f(request, *args, **kwargs)

        if isinstance(response, dict):
            return JsonResponse(response)
        else:
            return response

    return decorator(ajax)
