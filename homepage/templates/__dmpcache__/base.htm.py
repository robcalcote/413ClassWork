# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549483002.273069
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'navbar_main', 'site_title', 'site_left', 'site_center', 'site_right', 'footer_datetime']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def footer_datetime():
            return render_footer_datetime(context._locals(__M_locals))
        def site_title():
            return render_site_title(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n')
        __M_writer('        <title>Test - ')
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
        __M_writer('homepage/media/bootstrap-4.0.0-dist/css/bootstrap.min.css"/>\r\n        <script src="bootstrap-4.0.0-dist/js/bootstrap.min.js"></script>\r\n        \r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        <header>\r\n\r\n')
        __M_writer('            <div id="maintenance_message" class="alert alert-danger">\r\n                This page is under construction...\r\n            </div>\r\n\r\n')
        __M_writer('            <div id="navbar_main">\r\n                <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n')
        __M_writer('                    <a class="navbar-brand" href="#"></a>\r\n\r\n')
        __M_writer('                    <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                        <ul class="navbar-nav mr-auto">\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_main'):
            context['self'].navbar_main(**pageargs)
        

        __M_writer('\r\n                        </ul>\r\n                    </div>\r\n                </nav>\r\n            </div>\r\n        </header>\r\n\r\n        <main>\r\n')
        __M_writer('            <div id="site_title">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_title'):
            context['self'].site_title(**pageargs)
        

        __M_writer('\r\n            </div>\r\n\r\n')
        __M_writer('            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n\r\n\r\n        <footer>\r\n            ')
        __M_writer('\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_datetime'):
            context['self'].footer_datetime(**pageargs)
        

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


def render_navbar_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_main():
            return render_navbar_main(context)
        __M_writer = context.writer()
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


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_datetime(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_datetime():
            return render_footer_datetime(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 68, "20": 0, "41": 2, "42": 8, "47": 8, "48": 9, "49": 9, "50": 12, "51": 12, "52": 12, "53": 15, "54": 15, "55": 15, "56": 19, "57": 20, "58": 20, "59": 27, "60": 32, "61": 35, "62": 38, "67": 40, "68": 49, "73": 50, "74": 54, "79": 55, "84": 58, "89": 61, "90": 68, "95": 69, "101": 8, "112": 40, "123": 50, "134": 55, "145": 58, "156": 61, "167": 69, "178": 167}}
__M_END_METADATA
"""
