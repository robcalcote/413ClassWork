# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551047367.3662705
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'navbar_main', 'navbar_login', 'site_title', 'left_column', 'center_content', 'right_column']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar_login():
            return render_navbar_login(context._locals(__M_locals))
        true = context.get('true', UNDEFINED)
        def site_title():
            return render_site_title(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left_column():
            return render_left_column(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context._locals(__M_locals))
        Login = context.get('Login', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right_column():
            return render_right_column(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n')
        __M_writer('        <title>Sprint 1 - ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/django.png">  \r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/css/bootstrap.min.css"/>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/js/bootstrap.min.js"></script>\r\n        \r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n')
        __M_writer('        <div id="maintenance_message" class="alert alert-danger">\r\n            This page is under construction...\r\n        </div>\r\n\r\n        <br /><br /><br />\r\n        <header>\r\n')
        __M_writer('            <div id="navbar_main">\r\n                <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n')
        __M_writer('                    <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                        <ul class="navbar-nav mr-auto ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'AutoGrader' else '' ))
        __M_writer('">\r\n                            <li class="nav-item"><img class="site_icon" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/django.png"></a></li>\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_main'):
            context['self'].navbar_main(**pageargs)
        

        __M_writer('\r\n                        </ul>\r\n                        <div class="dropdown">\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_login'):
            context['self'].navbar_login(**pageargs)
        

        __M_writer('\r\n                        </div> \r\n                    </div>\r\n                </nav>\r\n            </div>\r\n        </header>\r\n\r\n        <main>\r\n')
        __M_writer('            <div id="site_title">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_title'):
            context['self'].site_title(**pageargs)
        

        __M_writer('\r\n            </div>\r\n\r\n')
        __M_writer('            <div id="left_column">\r\n')
        __M_writer('                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_column'):
            context['self'].left_column(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="center_content">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="right_column">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_column'):
            context['self'].right_column(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n\r\n\r\n        <footer>\r\n            <div id="footer_main">\r\n                ')
        __M_writer('\r\n                <p>Copyright &copy; ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.now().strftime('%Y') ))
        __M_writer(' Sprint 1</p><br/>\r\n            </div>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_main():
            return render_navbar_main(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_login(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        Login = context.get('Login', UNDEFINED)
        def navbar_login():
            return render_navbar_login(context)
        true = context.get('true', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if Login == true:
            __M_writer('                                    <a class="button btn btn-secondary" type="button" \r\n                                    id="dropdownMenuButton" href="/account/login/">Login</a>\r\n')
        else:
            __M_writer('                                    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                    Welcome, User (Change later)\r\n                                    </button>\r\n                                    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\r\n                                    <a class="dropdown-item" href="#">Your Account</a>\r\n                                    <a class="dropdown-item" href="#">Settings</a>\r\n                                    <a class="dropdown-item" href="/">Logout</a>\r\n')
        __M_writer('                                </div>\r\n                            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_title():
            return render_site_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_column():
            return render_left_column(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_column(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_column():
            return render_right_column(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 85, "20": 0, "44": 2, "45": 8, "50": 8, "51": 9, "52": 9, "53": 12, "54": 12, "55": 12, "56": 15, "57": 15, "58": 15, "59": 16, "60": 16, "61": 19, "62": 20, "63": 20, "64": 25, "65": 32, "66": 35, "67": 36, "68": 36, "69": 37, "70": 37, "75": 38, "80": 55, "81": 64, "86": 65, "87": 69, "88": 71, "93": 71, "98": 74, "103": 77, "104": 85, "105": 86, "106": 86, "112": 8, "123": 38, "134": 41, "142": 41, "143": 42, "144": 43, "145": 45, "146": 46, "147": 54, "153": 65, "164": 71, "175": 74, "186": 77, "197": 186}}
__M_END_METADATA
"""
