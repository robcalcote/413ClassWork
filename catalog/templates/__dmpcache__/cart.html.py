# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554063308.5705466
_enable_loop = True
_template_filename = 'C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        sale = context.get('sale', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def center_content():
            return render_center_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        cartItems = context.get('cartItems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center_content'):
            context['self'].center_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Your Cart')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cartItems = context.get('cartItems', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        def center_content():
            return render_center_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="shopping_cart">\r\n        <br />\r\n        <table>\r\n')
        __M_writer('            <tr>\r\n                <th>Product Image</th>\r\n                <th>Product Name</th>\r\n                <th>Quantity</th>\r\n                <th>Price</th>\r\n                <th>Extended</th>\r\n                <th>Actions</th>\r\n            </tr>\r\n')
        for si in cartItems:
            __M_writer('                <tr>   \r\n                    <td></td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.name ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.quantity ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.price ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.price * si.quantity ))
            __M_writer('</td>\r\n                    <td><a class="button" href="/catalog/cart.remove/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.id ))
            __M_writer('">Remove</a></td>\r\n                </tr>\r\n')
        __M_writer('            <tr><td></td><td></td><td></td>\r\n            <td></td><td></td><td></td></tr>\r\n            <tr>\r\n                <td></td>\r\n                <td>Subtotal</td>\r\n                <td></td><td></td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.subtotal ))
        __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n            <tr>\r\n                <td></td>\r\n                <td>Tax</td>\r\n                <td></td><td></td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.tax ))
        __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n            <tr><td></td><td></td><td></td>\r\n            <td></td><td></td><td></td></tr>\r\n            <tr>\r\n                <td></td>\r\n                <td>Total</td>\r\n                <td></td><td></td>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.total ))
        __M_writer('</td>\r\n                <td></td>\r\n            </tr>\r\n        </table>\r\n    </div>\r\n    <br />\r\n    <div id="checkout_button">\r\n        <a class="button btn btn-secondary" type="button" \r\n        id="dropdownMenuButton" href="/catalog/checkout/">Checkout Now</a>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Rob/Desktop/BYU/Winter2019/413/project2class/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 4, "56": 4, "62": 4, "68": 7, "77": 7, "78": 12, "79": 22, "80": 23, "81": 25, "82": 25, "83": 26, "84": 26, "85": 27, "86": 27, "87": 28, "88": 28, "89": 29, "90": 29, "91": 32, "92": 38, "93": 38, "94": 45, "95": 45, "96": 54, "97": 54, "103": 97}}
__M_END_METADATA
"""
