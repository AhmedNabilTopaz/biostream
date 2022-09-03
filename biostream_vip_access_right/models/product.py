# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.

from odoo import api, fields, models, _

from datetime import datetime, date,timedelta


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def calc_is_edit_sale_price(self):
        for rec in self:
            if self.env.user.has_group('biostream_vip_access_right.group_sale_price_edit'):
                self.is_edit_sale_price = True
            else:
                self.is_edit_sale_price = False

    is_edit_sale_price = fields.Boolean(string="IS Edit Price",compute='calc_is_edit_sale_price')


