# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552590441.7424748
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_title', 'left_column']


from catalog import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_title():
            return render_site_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_title'):
            context['self'].site_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_title():
            return render_site_title(context)
        __M_writer = context.writer()
        __M_writer('Sprint 3')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul id="category-list">\r\n        <li class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category is None else '' ))
        __M_writer('">\r\n            <a href="/catalog/index/">All Products</a></li>\r\n')
        for cat in cmod.Category.objects.order_by('name'):
            __M_writer('        <li class="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category == '${ cat.name }' else '' ))
            __M_writer('">\r\n            <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.id ))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.name ))
            __M_writer('</a></li>\r\n')
        __M_writer('    </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "42": 1, "43": 2, "48": 4, "53": 16, "59": 4, "65": 4, "71": 7, "79": 7, "80": 9, "81": 9, "82": 11, "83": 12, "84": 12, "85": 12, "86": 13, "87": 13, "88": 13, "89": 13, "90": 15, "96": 90}}
__M_END_METADATA
"""
