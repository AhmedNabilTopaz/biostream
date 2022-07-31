# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
import odoo.addons.decimal_precision as dp



class SalesRep(models.Model):
    _name = "sales.rep"
    _inherit = ['mail.thread']
    _rec_name = 'name'

    name = fields.Char(string="Name")

    message_follower_ids = fields.One2many(
        'mail.followers', 'res_id', string='Followers')
    message_ids = fields.One2many(
        'mail.message', 'res_id', string='Messages',
        domain=lambda self: [('message_type', '!=', 'user_notification')], auto_join=True)

    activity_ids = fields.One2many('mail.activity', 'calendar_event_id', string='Activities')
