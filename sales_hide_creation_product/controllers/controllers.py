# -*- coding: utf-8 -*-
# from odoo import http


# class SalesHideCreationProduct(http.Controller):
#     @http.route('/sales_hide_creation_product/sales_hide_creation_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_hide_creation_product/sales_hide_creation_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_hide_creation_product.listing', {
#             'root': '/sales_hide_creation_product/sales_hide_creation_product',
#             'objects': http.request.env['sales_hide_creation_product.sales_hide_creation_product'].search([]),
#         })

#     @http.route('/sales_hide_creation_product/sales_hide_creation_product/objects/<model("sales_hide_creation_product.sales_hide_creation_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_hide_creation_product.object', {
#             'object': obj
#         })
