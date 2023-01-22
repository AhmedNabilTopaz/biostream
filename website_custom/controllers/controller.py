# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import route,request
from odoo.tools.translate import _
from odoo.addons.website_sale.controllers.main import WebsiteSale

import logging
_logger = logging.getLogger(__name__)

class WebsiteAddress(WebsiteSale):
    def _get_mandatory_fields_billing(self, country_id=False):
        # req = ["name", "email", "street", "city", "country_id"]
        req = ["name","street", "state_id", "country_id"]
        if country_id:
            country = request.env['res.country'].browse(country_id)
            if country.state_required:
                req += ['state_id']
            # if country.zip_required:
            #     req += ['zip']
        return req

    def _get_mandatory_fields_shipping(self, country_id=False):
        # req = ["name", "street", "city", "country_id"]
        req = ["name", "street", "state_id", "country_id"]
        if country_id:
            country = request.env['res.country'].browse(country_id)
            if country.state_required:
                req += ['state_id']
            # if country.zip_required:
            #     req += ['zip']
        return req