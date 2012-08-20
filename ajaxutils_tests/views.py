def simple(request):
    return {'status': 'success'}


def simple_with_custom_status_code(request, status_code):
    return {'status': 'success'}, int(status_code)
