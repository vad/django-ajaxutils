from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('ajaxutils_tests.views',
    url(r'^simple/$', 'simple'),
    url(r'^simple_get/$', 'simple_get'),
    url(r'^simple_post/$', 'simple_post'),
    url(r'^logged/$', 'logged'),
)
