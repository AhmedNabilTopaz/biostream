# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

from odoo.exceptions import ValidationError


class AccountMove(models.Model):
	_inherit = 'account.move'

	state_id = fields.Many2one('res.country.state',string="State",tracking=True)
	city = fields.Char(string="City",tracking=True)

	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		res = super(AccountMove, self)._onchange_partner_id()
		if self.partner_id:
			self.state_id = self.partner_id.state_id.id
			self.city = self.partner_id.city
		return res



