# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    medical_rep_id = fields.Many2one('medical.rep', string="Medical Rep.")

