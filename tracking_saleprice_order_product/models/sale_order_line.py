# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.

from odoo import api, fields, models, _

from datetime import datetime, date,timedelta


class ProductTemplate(models.Model):
    _inherit = "product.template"

    list_price = fields.Float('Sales Price', default=1.0,digits='Product Price',help="Price at which the product is sold to customers.",tracking=True)






class SaleOrderline(models.Model):
    _inherit = "sale.order.line"


    def format_date(self, date):
        date_new = date + timedelta(hours=3)
        return date_new.strftime("%Y-%m-%d %H:%M:%S")

    @api.model
    def create(self, vals):
        res = super(SaleOrderline, self).create(vals)
        now = self.format_date(fields.Datetime.now())
        content = "Line Added by : " + str(self.env.user.name) + " - At : " + str(now) + "<br/>"
        if vals.get("product_id"):
            product = self.env['product.product'].sudo().browse(vals.get("product_id"))
            content = content + "  \u2022 Product : " + str(product.name) + "<br/>"

        if vals.get("name"):
            content = content + "  \u2022 Description: " + str(vals.get("name")) + "<br/>"

        if vals.get("product_uom_qty"):
            content = content + "  \u2022 Quantity Is: " + str(vals.get("product_uom_qty")) + "<br/>"

        if vals.get("default_product_price"):
            content = content + "  \u2022 سعر الجمهور :  " + str(vals.get("default_product_price")) + "<br/>"

        if vals.get("price_unit"):
            content = content + "  \u2022 سعر الصيدلي :  " + str(vals.get("price_unit")) + "<br/>"

        if vals.get("price_diff"):
            content = content + "  \u2022 Discount: " + str(vals.get("price_diff")) + "<br/>"


        res.order_id.message_post(body=content)

        return res

    def write(self, vals):
        print("FFFFFFF",vals)
        res = super(SaleOrderline, self).write(vals)
        now = self.format_date(fields.Datetime.now())
        content = "Line Update by : " + str(self.env.user.name) + " - At : "+ str(now)+ "<br/>"

        if vals.get("product_id"):
            product = self.env['product.product'].sudo().browse(vals.get("product_id"))
            content = content + "  \u2022 Product changed To  : " + str(product.name) + "<br/>"

        if vals.get("name"):
            # content = content + "  \u2022 Name changed from :  " + str(self.name) + " >>> "+ str(vals.get("name")) + "<br/>"
            content = content + "  \u2022 Description changed To :  " + " >>> "+ str(vals.get("name")) + "<br/>"

        if vals.get("product_uom_qty"):
            content = content + "  \u2022 Quantity changed to: " + str(vals.get("product_uom_qty")) + "<br/>"

        if vals.get("default_product_price"):
            content = content + "  \u2022 سعر الجمهور :  " + str(vals.get("default_product_price")) + "<br/>"

        if vals.get("price_unit"):
            content = content + "  \u2022 سعر الصيدلي :  " + str(vals.get("price_unit")) + "<br/>"

        if vals.get("price_diff"):
            content = content + "  \u2022 Discount: " + str(vals.get("price_diff")) + "<br/>"


        self.order_id.message_post(body=content)

        return res



    def unlink(self):
        active_id = self._context.get('active_id')
        print("$$$$$$$",self)
        order_line = self
        now = self.format_date(fields.Datetime.now())
        if order_line:
            for rec in order_line:
                content = "Line Deleted by : " + str(self.env.user.name) + " - At : " + str(now) + "<br/>"

                if rec.product_id:
                    content = content + "  \u2022 Deleted Product is : " + str(rec.product_id.name) + "<br/>"

                if rec.name:
                    content = content + "  \u2022 Deleted Description  is  :  " + " >>> " + str(rec.name) + "<br/>"

                if rec.product_uom_qty:
                    content = content + "  \u2022 Deleted Quantity is : " + str(rec.product_uom_qty) + "<br/>"

                if rec.default_product_price:
                    content = content + "  \u2022  Deleted سعر الجمهور :  " + str(rec.default_product_price) + "<br/>"

                if rec.price_unit:
                    content = content + "  \u2022 Deleted سعر الصيدلي :  " + str(rec.price_unit) + "<br/>"

                if rec.price_diff:
                    content = content + "  \u2022 Deleted Discount is: " + str(rec.price_diff) + "<br/>"

                rec.order_id.message_post(body=content)
        result = super(SaleOrderline, self).unlink()
        print("LLLLLLL",result)
        return result
