# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549511349.1616285
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
        def left_column():
            return render_left_column(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <li class="nav-item"><img class="site_icon" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/django.png"></a></li>\r\n    <li class="nav-item ')
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
        __M_writer('\r\n  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n    Welcome, User\r\n  </button>\r\n  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\r\n    <a class="dropdown-item" href="#">Your Account</a>\r\n    <a class="dropdown-item" href="#">Settings</a>\r\n    <a class="dropdown-item" href="#">Logout</a>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def left_column():
            return render_left_column(context)
        self = context.get('self', UNDEFINED)
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
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 13, "53": 24, "58": 33, "64": 5, "73": 5, "74": 6, "75": 6, "76": 7, "77": 7, "78": 9, "79": 9, "80": 11, "81": 11, "87": 15, "93": 15, "99": 26, "107": 26, "108": 27, "109": 27, "110": 29, "111": 29, "112": 31, "113": 31, "119": 113}}
__M_END_METADATA
"""
