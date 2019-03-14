# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552536414.0648808
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/index.html'
_template_uri = 'index.html'
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
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def center_content():
            return render_center_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Catalog')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def center_content():
            return render_center_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p id="catalog-category">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'All Categories' if category is None else category.name ))
        __M_writer('</p>\r\n    <div id="catalog-products">\r\n')
        for prod in products:
            __M_writer('            <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prod.id ))
            __M_writer('"></span>\r\n')
        __M_writer('    </div>\r\n    <br/>\r\n    <br/>\r\n    <div id="pagination_buttons">\r\n')
        if (page == numpages) & (page < 2):
            __M_writer('        <p>All products shown.</p>\r\n')
        elif page < 2:
            __M_writer('        <button type="button" class="pagination_button">\r\n            <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '-' if category is None else category.id ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 ))
            __M_writer('">Next Page</a>\r\n        </button>\r\n')
        elif page == numpages:
            __M_writer('        <button type="button" class="pagination_button">\r\n            <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '-' if category is None else category.id ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 ))
            __M_writer('">Previous Page</a>\r\n        </button>\r\n')
        else:
            __M_writer('        <button type="button" class="pagination_button">\r\n            <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '-' if category is None else category.id ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 ))
            __M_writer('">Previous Page</a>\r\n        </button>\r\n        <button type="button" class="pagination_button">\r\n            <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( '-' if category is None else category.id ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 ))
            __M_writer('">Next Page</a>\r\n        </button>\r\n')
        __M_writer('    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 4, "53": 36, "59": 4, "65": 4, "71": 7, "82": 7, "83": 8, "84": 8, "85": 10, "86": 11, "87": 11, "88": 11, "89": 13, "90": 17, "91": 18, "92": 19, "93": 20, "94": 21, "95": 21, "96": 21, "97": 21, "98": 23, "99": 24, "100": 25, "101": 25, "102": 25, "103": 25, "104": 27, "105": 28, "106": 29, "107": 29, "108": 29, "109": 29, "110": 32, "111": 32, "112": 32, "113": 32, "114": 35, "120": 114}}
__M_END_METADATA
"""
