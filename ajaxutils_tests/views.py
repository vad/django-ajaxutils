def simple(request):
    return {'status': 'success'}


def raise_404(request):
    from django.http import Http404

    raise Http404


def simple_with_custom_status_code(request, status_code):
    return {'status': 'success'}, int(status_code)
