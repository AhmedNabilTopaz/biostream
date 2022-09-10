# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state_id = fields.Many2one('res.country.state', string="State", tracking=True)
    city = fields.Char(string="City", tracking=True)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(SaleOrder, self).onchange_partner_id()
        if self.partner_id:
            self.state_id = self.partner_id.state_id.id
            self.city = self.partner_id.city
        return res


class SaleReport(models.Model):
    _inherit = "sale.report"

    state_id = fields.Many2one('res.country.state', string="State", tracking=True)
    city = fields.Char(string="City", tracking=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['state_id'] = ',s.state_id as state_id'
        fields['city'] = ',s.city as city'
        groupby += ',s.state_id,s.city'

        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
