try:
    import simplejson as json
except ImportError:
    import json

from django.http import HttpResponse


class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with
    ``application/json`` mimetype.
    """

    def __init__(self, data, mimetype='application/json', status=200):
        super(JsonResponse, self).__init__(
            content=json.dumps(data),
            mimetype=mimetype,
            status=status
        )
