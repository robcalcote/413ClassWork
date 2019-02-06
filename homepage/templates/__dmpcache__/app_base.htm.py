# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549481988.3948832
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['navbar_main', 'footer_datetime']


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
        request = context.get('request', UNDEFINED)
        def footer_datetime():
            return render_footer_datetime(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_main'):
            context['self'].navbar_main(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_datetime'):
            context['self'].footer_datetime(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def navbar_main():
            return render_navbar_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/">Home</a></li>\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/about/">About</a></li>\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/contact/">Contact</a></li>\r\n    <li class="nav-item dropdown">\r\n        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"\r\n            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n            Dropdown\r\n        </a>\r\n        <div class="dropdown-menu" aria-labelledby="navbarDropdown">\r\n            <a class="dropdown-item" href="#">Action</a>\r\n            <a class="dropdown-item" href="#">Another action</a>\r\n            <div class="dropdown-divider"></div>\r\n            <a class="dropdown-item" href="#">Something else here</a>\r\n        </div>\r\n    </li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_datetime(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_datetime():
            return render_footer_datetime(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 24, "50": 29, "56": 5, "64": 5, "65": 6, "66": 6, "67": 8, "68": 8, "69": 10, "70": 10, "76": 27, "82": 27, "88": 82}}
__M_END_METADATA
"""
