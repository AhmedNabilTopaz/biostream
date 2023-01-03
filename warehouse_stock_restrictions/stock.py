# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning
from odoo.exceptions import UserError, ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    restrict_locations = fields.Boolean('Restrict Location')

    stock_location_ids = fields.Many2many(
        'stock.location',
        'location_security_stock_location_users',
        'user_id',
        'location_id',
        'Stock Locations')

    default_picking_type_ids = fields.Many2many(
        'stock.picking.type', 'stock_picking_type_users_rel',
        'user_id', 'picking_type_id', string='Default Warehouse Operations')


class stockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.onchange('picking_type_id', 'partner_id')
    def onchange_picking_type(self):
        # res = super(stockPicking, self).onchange_picking_type()
        if self.picking_type_id:
            if self.picking_type_id.code == 'internal':
                print("test",self.location_id)
                self.location_id = self.picking_type_id.default_location_src_id.id
                self.code = 'internal'
        # return res
    code = fields.Char(string="Code")

    location_id = fields.Many2one(
        'stock.location', "Source Location",
        default=lambda self: self.env['stock.picking.type'].browse(
            self._context.get('default_picking_type_id')).default_location_src_id,
        check_company=True,required=False,
        states={'draft': [('readonly', False)]})

    # default = lambda self: self.env['stock.picking.type'].browse(
    #     self._context.get('default_picking_type_id')).default_location_src_id

    def button_validate(self):
        res = super(stockPicking, self).button_validate()
        lst= []
        if self.env.user.stock_location_ids:
            for rec in self.env.user.stock_location_ids:

                lst.append(rec.id)


            if self.location_dest_id.id not in lst:
                raise ValidationError("Destination Location Must be available for you")

        return res



#     @api.constrains('state', 'location_id', 'location_dest_id')
#     def check_user_location_rights(self):
#         self.ensure_one()
#         if self.state == 'draft':
#             return True
#         user_locations = self.env.user.stock_location_ids
#         print(user_locations)
#         print("Checking access %s" %self.env.user.default_picking_type_ids)
#         if self.env.user.restrict_locations:
#             message = _(
#                 'Invalid Location. You cannot process this move since you do '
#                 'not control the location "%s". '
#                 'Please contact your Adminstrator.')
#             if self.location_id not in user_locations:
#                 raise Warning(message % self.location_id.name)
#             elif self.location_dest_id not in user_locations:
#                 raise Warning(message % self.location_dest_id.name)


