# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import time
from ast import literal_eval
from datetime import date, timedelta
from itertools import groupby
from operator import attrgetter, itemgetter
from collections import defaultdict

from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, format_datetime
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.tools.misc import format_date
from odoo.exceptions import UserError, ValidationError, AccessError, RedirectWarning




class Picking(models.Model):
    _inherit = "stock.picking"


    def button_validate(self):
        for picking in self:
            if picking.picking_type_code and picking.picking_type_code == 'incoming':
                for line in picking.move_lines:
                    if line.quantity_done> line.product_qty and not line.product_id.allow_receiving_more:
                        raise ValidationError(
                            _('Done Quantity cannot exceed the Orderd Quaintity of {productname}'.format(
                                productname=line.product_id.display_name)))

            elif picking.picking_type_code and picking.picking_type_code == 'outgoing':
                for line in picking.move_lines:
                    if line.quantity_done> line.product_qty and not line.product_id.allow_delivery_more:
                        raise ValidationError(
                            _('Done Quantity cannot exceed the Orderd Quaintity of {productname}'.format(
                                productname=line.product_id.display_name)))

        return super().button_validate()
