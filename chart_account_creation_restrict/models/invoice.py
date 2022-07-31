# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare

from itertools import groupby

class AccountAccount(models.Model):
    _inherit = "account.account"

    account_excl_check = fields.Boolean(string="Account Exclude Check")


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    account_excl_check = fields.Boolean(string="Account Exclude Check")
