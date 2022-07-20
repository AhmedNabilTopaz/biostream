from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):

    _inherit = "account.move"

    show_tax = fields.Boolean(string="Show Tax")

class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    default_product_price  = fields.Float(string="Price Before",related='product_id.list_price')

    @api.depends('default_product_price','price_unit')
    def calc_pricee_diff(self):
        for rec in self:
            if rec.product_id.list_price > rec.price_unit:
                rec.price_diff = rec.product_id.list_price - rec.price_unit
            else:
                rec.price_diff = rec.price_unit - rec.product_id.list_price

    price_diff = fields.Float(string="Discount",compute='calc_pricee_diff')

