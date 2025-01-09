from odoo import api, fields, models


class salesTopaz(models.Model):
    # Inherit Sale Order from Sale Module

    _inherit = 'sale.order'
    is_delivered=fields.Boolean('Is Delivered',compute='compute_is_delivered',defualt=False)
    # Add new fields in the Quotations create menu

    sales_man_id = fields.Many2one('hr.employee',
                               'Sales Man')
    sales_supervisor_id = fields.Many2one('hr.employee',
                                      'Sales Supervisor')


    def compute_is_delivered(self):
        for order in self:
            order.is_delivered = False
            for pick in order.picking_ids:
                if pick.state=='done':
                    order.is_delivered=True
class SalesOrderLine(models.Model):
    _inherit = 'sale.order.line'
    available_qty = fields.Float(
        string="Available Quantity",
        compute="_compute_available_qty",
    )

    @api.depends('product_id', 'product_uom_qty', 'order_id.warehouse_id')
    def _compute_available_qty(self):
        for line in self:
            if line.product_id :
                # Get stock location tied to the selected warehouse
                stock_location = line.order_id.warehouse_id.lot_stock_id
                # if stock_location:
                    # Compute the available quantity from stock quants
                quants = self.env['stock.quant'].search([
                    ('product_id', '=', line.product_id.id),
                    ('location_id', '=', stock_location.id)
                ])
                line.available_qty = sum(quants.mapped('available_quantity'))
            else:
                line.available_qty = 0.0
                # else:
            #     line.available_qty = 0.0
