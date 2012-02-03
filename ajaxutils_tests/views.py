from ajaxutils.decorators import ajax


@ajax()
def simple(request):
    return {'status': 'success'}


@ajax(login_required=True)
def logged(request):
    return {'status': 'success'}
