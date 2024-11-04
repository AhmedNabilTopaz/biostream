# Copyright 2015-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models



class ProductTemplate(models.Model):
    _inherit = "product.template"

    allow_receiving_more = fields.Boolean(string='Receiving more QTY',
        help="If this enabled , Users can receive more than Purchase  ordered quantity"
    )
    allow_delivery_more = fields.Boolean(string='Delivering more QTY',
                                          help="If this enabled , Users can delivery more than Sale  ordered "
                                               "quantity"
                                          )
