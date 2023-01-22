# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.

from odoo import models, api,fields ,_
from odoo.exceptions import UserError


class SaleOrderline(models.Model):
    _inherit = "sale.order.line"


    def calc_is_change_price_unit(self):
        if self.env.user.has_group('restrict_saleprice_change.groups_restrict_price_change'):
            self.is_change_price_unit = True
        else:
            self.is_change_price_unit = False

    is_change_price_unit = fields.Boolean(string='Is Change Price',compute='calc_is_change_price_unit')
