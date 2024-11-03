import base64
import collections
import datetime
import hashlib
import pytz
import threading
import re

import requests
from collections import defaultdict
from lxml import etree
from random import randint
from werkzeug import urls

from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command
from odoo.osv.expression import get_unaccent_wrapper
from odoo.exceptions import RedirectWarning, UserError, ValidationError

class Partner(models.Model):
    _inherit = "res.partner"


    @api.onchange('parent_id')
    def onchange_parent_id(self):
        self.vat='27607251201430'
        return super(Partner, self).onchange_parent_id()

        # # return values in result, as this method is used by _fields_sync()
        # if not self.parent_id:
        #     return
        # result = {}
        # partner = self._origin
        # if partner.parent_id and partner.parent_id != self.parent_id:
        #     result['warning'] = {
        #         'title': _('Warning'),
        #         'message': _('Changing the company of a contact should only be done if it '
        #                      'was never correctly set. If an existing contact starts working for a new '
        #                      'company then a new contact should be created under that new '
        #                      'company. You can use the "Discard" button to abandon this change.')}
        # if partner.type == 'contact' or self.type == 'contact':
        #     # for contacts: copy the parent address, if set (aka, at least one
        #     # value is set in the address: otherwise, keep the one from the
        #     # contact)
        #     address_fields = self._address_fields()
        #     if any(self.parent_id[key] for key in address_fields):
        #         def convert(value):
        #             return value.id if isinstance(value, models.BaseModel) else value
        #         result['value'] = {key: convert(self.parent_id[key]) for key in address_fields}
        # return result