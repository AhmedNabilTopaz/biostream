from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    # product_tmpl_id = fields.Many2one('product.template', 'Product Template', related='product_id.product_tmpl_id')





