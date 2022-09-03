# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.

from odoo import api, fields, models, _,SUPERUSER_ID
from lxml import etree


from datetime import datetime, date,timedelta


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def calc_is_edit_sale_price(self):
        for rec in self:
            if self.env.user.has_group('biostream_vip_access_right.group_sale_price_edit'):
                self.is_edit_sale_price = True
            else:
                self.is_edit_sale_price = False

    is_edit_sale_price = fields.Boolean(string="IS Edit Price",compute='calc_is_edit_sale_price')



    def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False):
        res = super(ProductTemplate, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=False)

        group_id = self.env.user.has_group('biostream_vip_access_right.product_template_creation_restriction_group')

        doc = etree.XML(res['arch'])

        # if group_id and self.env.uid != 2:
        print("KKKKKKK",group_id)
        if not group_id:

            if view_type == 'tree' or view_type == 'form'or view_type == 'kanban' :

                nodes_tree = doc.xpath("//tree[@string='Product']")
                print("1111111",nodes_tree)

                for node in nodes_tree:
                    print("RRRRRRR",node)
                    node.set('create', '0')
                    # node.set('edit', '0')

                nodes_form = doc.xpath("//form[@string='Product']")
                print("222222222",nodes_form)

                for node in nodes_form:
                    print("EEEEEEEEE",node)
                    node.set('create', '0')
                    node.set('edit', '0')

                nodes_kanban = doc.xpath("//kanban")
                for node in nodes_kanban:
                    print("%%%%%%%%%%%%%",node)
                    node.set('create', '0')

                res['arch'] = etree.tostring(doc)

        return res


