from odoo import fields, models



class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    fb_pixel_property_content_ids_type = fields.Selection(
        related='website_id.fb_pixel_property_content_ids_type',
        readonly=False,
    )
