from odoo import api, fields, models



class Website(models.Model):
    _inherit = "website"

    fb_pixel_property_content_ids_type = fields.Selection(
        selection=[
            ('template_id', 'Product Template ID'),
            ('name', 'Product Template Name'),
            ('product_id', 'Product ID'),
        ],
        string='content_ids',
        default='template_id',
    )

    @api.model
    def sanitize_name(self, name):
        return name.replace("'", "")
