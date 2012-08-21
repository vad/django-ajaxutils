from django.http import HttpResponse

from ajaxutils import json


def handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError,\
        'Object of type %s with value of %s is not JSON serializable' % (
            type(obj), repr(obj)
            )


class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with
    ``application/json`` mimetype.
    """

    def __init__(self, data, mimetype='application/json', status=200):
        super(JsonResponse, self).__init__(
            content=json.dumps(data, default=handler),
            mimetype=mimetype,
            status=status
        )
