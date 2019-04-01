# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554092128.905591
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'center_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        sale_total = context.get('sale_total', UNDEFINED)
        self = context.get('self', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Checkout')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        sale_total = context.get('sale_total', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def center_content():
            return render_center_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <br />\r\n    <div class="checkout-form">\r\n        <form method="post">\r\n            <table>\r\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n')
        __M_writer('                <script\r\n                    src="https://checkout.stripe.com/checkout.js" class="stripe-button"\r\n                    data-key="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STRIPE_PUBLIC_KEY ))
        __M_writer('"\r\n                    data-amount="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale_total ))
        __M_writer('"\r\n                    data-name="Sprint4"\r\n                    data-description="Fill this out to send the data to Stripe!"\r\n                    data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n                    data-locale="auto">\r\n                </script>\r\n            </table>\r\n        </form>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 4, "57": 4, "63": 4, "69": 7, "79": 7, "80": 12, "81": 12, "82": 14, "83": 16, "84": 16, "85": 17, "86": 17, "92": 86}}
__M_END_METADATA
"""
