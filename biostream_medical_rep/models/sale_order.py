# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    medical_rep_id = fields.Many2one('medical.rep', string="Medical Rep.")

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(SaleOrder, self).onchange_partner_id()
        if self.partner_id:
            self.medical_rep_id = self.partner_id.medical_rep_id.id
        return res
