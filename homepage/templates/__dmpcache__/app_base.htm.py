# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550968141.6693337
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['navbar_main', 'navbar_login', 'left_column']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context._locals(__M_locals))
        def navbar_login():
            return render_navbar_login(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_main'):
            context['self'].navbar_main(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_login'):
            context['self'].navbar_login(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/">Home</a></li>\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/about/">About</a></li>\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/contact/">Contact</a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_login():
            return render_navbar_login(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <a class="nav-link" href="/account/login/">\r\n    <button class="btn btn-secondary" type="button" id="dropdownMenuButton">\r\n      Login\r\n    </button>\r\n  </a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/">Home</a></p>\r\n    <p class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/about/">About</a></p>\r\n    <p class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/contact/">Contact</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 12, "52": 20, "57": 29, "63": 5, "71": 5, "72": 6, "73": 6, "74": 8, "75": 8, "76": 10, "77": 10, "83": 14, "89": 14, "95": 22, "103": 22, "104": 23, "105": 23, "106": 25, "107": 25, "108": 27, "109": 27, "115": 109}}
__M_END_METADATA
"""
