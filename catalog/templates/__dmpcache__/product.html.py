# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553977100.5933995
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['center_content']


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
        self = context.get('self', UNDEFINED)
        product = context.get('product', UNDEFINED)
        allImages = context.get('allImages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def center_content():
            return render_center_content(context)
        self = context.get('self', UNDEFINED)
        product = context.get('product', UNDEFINED)
        allImages = context.get('allImages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="product-display">\r\n        <div class="product-image-main"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.image_url() ))
        __M_writer('" />\r\n            <div class="product-display-below">\r\n')
        for images in allImages:
            __M_writer('                    <img class="product-image-alt" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( images.image_url() ))
            __M_writer('" />\r\n')
        __M_writer('            </div>\r\n        </div>\r\n        <div class="product-info-main">\r\n            <table>\r\n                <tr><th></th><th></th></tr>\r\n                <tr><td>Name:</td><td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        __M_writer('</td></tr>\r\n                <tr><td>Price:</td><td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.price ))
        __M_writer('</td></tr>\r\n                <tr><td>Description:</td><td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.description ))
        __M_writer('</td></tr>\r\n                <tr><td>Quantity Available:</td><td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.quantity ))
        __M_writer('</td></tr>\r\n            </table>\r\n            <br />\r\n            <div class="buy-now-form">\r\n                <form method="post">\r\n                    <table>\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n                    </table>\r\n                    <input type="submit" value="Buy Now" />\r\n                </form>\r\n            </div>\r\n        </div>\r\n        <br />\r\n        <br />\r\n\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 4, "60": 4, "61": 6, "62": 6, "63": 8, "64": 9, "65": 9, "66": 9, "67": 11, "68": 16, "69": 16, "70": 17, "71": 17, "72": 18, "73": 18, "74": 19, "75": 19, "76": 25, "77": 25, "83": 77}}
__M_END_METADATA
"""
