# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549312997.348484
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'navbar_items', 'site_left', 'site_center', 'site_right']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n')
        __M_writer('        <title>Test - ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/pythonicon.png">  \r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-dist/css/bootstrap.min.css"/>\r\n        <script src="bootstrap-4.0.0-dist/js/bootstrap.min.js"></script>\r\n        \r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <div id="maintenance_message" class="alert alert-danger">\r\n            This page is under construction...\r\n        </div>\r\n\r\n        <header>\r\n            <nav class="navbar navbar-expand-md navbar-light bg-light">\r\n                <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">\r\n                    <ul class="navbar-nav mr-auto"> \r\n                        <li class="nav-item">\r\n                            <a class="nav-link" href="/"></li><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/site.ico" alt="Logo" class="navbar-image"/></a>\r\n                        </li>\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n                    </ul>\r\n                </div>\r\n                <div class="mx-auto order-0">\r\n                    <a class="navbar-brand mx-auto" href="#">Navbar 2</a>\r\n                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".dual-collapse2">\r\n                        <span class="navbar-toggler-icon"></span>\r\n                    </button>\r\n                </div>\r\n                <div class="navbar-collapse collapse w-100 order-3 dual-collapse2" style="padding-right: 60px">\r\n                    <ul class="navbar-nav ml-auto">\r\n                        <li class="dropdown nav-item">\r\n<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n          Dropdown\r\n        </a>\r\n                            <ul class="dropdown-menu" style="text-align: center">\r\n                                <li><a href="#">Account</a></li>\r\n                                <li><a href="#">Settings</a></li>\r\n                                <li><a href="#">Sign Out</a></li>\r\n                            </ul>\r\n                        </li>\r\n                    </ul>\r\n                </div>\r\n            </nav>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n\r\n\r\n        <footer>\r\n            ')
        __M_writer('\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
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


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    Left Side\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    Right Side\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 84, "20": 0, "37": 2, "38": 8, "43": 8, "44": 9, "45": 9, "46": 12, "47": 12, "48": 12, "49": 15, "50": 15, "51": 15, "52": 19, "53": 20, "54": 20, "55": 34, "56": 34, "61": 36, "66": 67, "71": 72, "76": 77, "77": 84, "83": 8, "94": 36, "105": 65, "111": 65, "117": 70, "123": 70, "129": 75, "135": 75, "141": 135}}
__M_END_METADATA
"""
