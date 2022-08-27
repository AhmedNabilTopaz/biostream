# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_rep_id = fields.Many2one('sales.rep', string="Sales Rep.")

