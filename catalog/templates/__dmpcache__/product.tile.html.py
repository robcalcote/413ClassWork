# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552527126.702222
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/product.tile.html'
_template_uri = 'product.tile.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
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
        self = context.get('self', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <a href="/catalog/product/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
        __M_writer('">\r\n        <div class="product-tile">\r\n            <div><img class="product-image" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.image_url() ))
        __M_writer('" /></div>\r\n            <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        __M_writer('</div>\r\n            <div class="product-price">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.price ))
        __M_writer('</div>\r\n        </div>\r\n    </a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/product.tile.html", "uri": "product.tile.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 4, "58": 4, "59": 6, "60": 6, "61": 7, "62": 7, "63": 8, "64": 8, "70": 64}}
__M_END_METADATA
"""
