from django.conf.urls.defaults import patterns, url

from .views import simple, simple_with_custom_status_code, raise_404

from ajaxutils.decorators import ajax


urlpatterns = patterns('ajaxutils_tests.views',
    url(r'^simple/$', ajax()(simple)),
    url(r'^simple_bool_get/$', ajax(require_GET=True)(simple)),
    url(r'^simple_get_and_post/$', ajax(methods=["get", "post"])(simple)),
    url(r'^simple_get/$', ajax(require="GET")(simple)),
    url(r'^simple_bool_post/$', ajax(require_POST=True)(simple)),
    url(r'^simple_post/$', ajax(require="POST")(simple)),
    url(r'^logged/$', ajax(login_required=True)(simple)),

    url(r'^raise/404/$', ajax()(raise_404)),

    url(
        r'^custom/(?P<status_code>\d+)/$',
        ajax()(simple_with_custom_status_code)
    ),
)
