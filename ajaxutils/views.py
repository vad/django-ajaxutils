"""
Class based views
"""
from .decorators import ajax

from django.views.generic.base import View


class AjaxMixin(object):
    """
    This mixin wraps all the methods of the view in the
    ajaxutils.decorators.ajax() decorator.

    WARNING: this will change! It's just a prototype.
    """

AjaxMixin.dispatch = ajax()(View.dispatch.im_func)
