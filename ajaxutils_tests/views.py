from ajaxutils.decorators import ajax


@ajax()
def simple(request):
    return {'status': 'success'}


@ajax(login_required=True)
def logged(request):
    return {'status': 'success'}


@ajax(require_GET=True)
def simple_get(request):
    return {'status': 'success'}


@ajax(require_POST=True)
def simple_post(request):
    return {'status': 'success'}
