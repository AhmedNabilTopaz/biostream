# -*- coding: utf-8 -*-

from openerp import models, fields, api

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_rep_id = fields.Many2one('sales.rep', string="Sales Rep.")



# class SaleReport(models.Model):
#     _inherit = "sale.report"
#
#
#     sale_rep_id = fields.Many2one('sales.rep', string="Sales Rep.")
#
#     def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
#         fields['sale_rep_id'] = ',s.sale_rep_id as sale_rep_id'
#         groupby += ',s.sale_outdoor_id'
#
#         return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
