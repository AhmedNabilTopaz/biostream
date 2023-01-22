from odoo import api, fields, models
from itertools import groupby


# from odoo.exceptions import ValidationError

class AccountFollowupReport():
    _inherit = 'account.followup.report'

    @api.model
    def send_email(self, options):
        """
        Send by mail the followup to the customer
        """
        partner = self.env['res.partner'].browse(options.get('partner_id'))
        non_blocked_amls = partner.unreconciled_aml_ids.filtered(lambda aml: not aml.blocked)
        if not non_blocked_amls:
            return True
        non_printed_invoices = partner.unpaid_invoices.filtered(lambda inv: not inv.message_main_attachment_id)
        if non_printed_invoices and partner.followup_level.join_invoices:
            raise UserError(
                _('You are trying to send a followup report to a partner for which you didn\'t print all the invoices ({})').format(
                    " ".join(non_printed_invoices.mapped('name'))))
        invoice_partner = self.env['res.partner'].browse(partner.address_get(['invoice'])['invoice'])
        email = invoice_partner.email
        if email and email.strip():
            self = self.with_context(lang=partner.lang or self.env.user.lang)
            # When printing we need te replace the \n of the summary by <br /> tags
            body_html = self.with_context(print_mode=True, mail=True).get_html(options)
            body_html = body_html.replace('o_account_reports_edit_summary_pencil',
                                          'o_account_reports_edit_summary_pencil d-none')
            start_index = body_html.find('<span>', body_html.find('<div class="o_account_reports_summary">'))
            end_index = start_index > -1 and body_html.find('</span>', start_index) or -1
            if end_index > -1:
                replaced_msg = body_html[start_index:end_index].replace('\n', '')
                body_html = body_html[:start_index] + replaced_msg + body_html[end_index:]
            print(">D>D>D>D>D>D>>>@22")
            partner.with_context(mail_post_autofollow=True, lang=partner.lang or self.env.user.lang).message_post(
                partner_ids=[invoice_partner.id],
                body=body_html,
                subject=self._get_report_manager(options).email_subject,
                subtype_id=self.env.ref('mail.mt_note').id,
                model_description=_('payment reminder'),
                email_layout_xmlid='mail.mail_notification_light',
                attachment_ids=partner.followup_level.join_invoices and partner.unpaid_invoices.message_main_attachment_id.ids or [],
            )
            for ppp in self.followup_level.accountant_ids.ids:
                partner.with_context(mail_post_autofollow=True, lang=partner.lang or self.env.user.lang).message_post(
                    partner_ids=[ppp],
                    body=body_html,
                    subject=self._get_report_manager(options).email_subject,
                    subtype_id=self.env.ref('mail.mt_note').id,
                    model_description=_('payment reminder'),
                    email_layout_xmlid='mail.mail_notification_light',
                    attachment_ids=partner.followup_level.join_invoices and partner.unpaid_invoices.message_main_attachment_id.ids or [],
                )
            return True
        raise UserError(_('Could not send mail to partner %s because it does not have any email address defined',
                          partner.display_name))


class FollowupLine(models.Model):
    _inherit = 'account_followup.followup.line'
    accountant_ids = fields.Many2many(comodel_name="res.partner", relation="accounts_partner", column1="", column2="",
                                      string="Accounts", )


class StockPicing(models.Model):
    _inherit = 'stock.picking'

    extra_lines_ids = fields.One2many(comodel_name="stock.picking.extra.lines", inverse_name="stock_picking_id", string="Lines",
                                required=False, )

    @api.onchange('move_ids_without_package')
    def onchange_move_lines_kits(self):
        lines=[]
        for line in self.move_ids_without_package:
            lines.append((0,0,{
                'product_line_id':line.product_id.id,
                'product_uom_qty':line.product_uom_qty,
                'product_uom':line.product_uom.id,
            }))
        print(":::>>",lines)
        self.extra_lines_ids=[(5,0,0)]
        self.extra_lines_ids=lines


class StockPickingExtraLines(models.Model):
    _name = 'stock.picking.extra.lines'

    stock_picking_id = fields.Many2one(comodel_name="stock.picking", string="", required=False, )
    product_line_id = fields.Many2one(comodel_name="product.product", string="Product", required=False, )
    product_uom_qty = fields.Float(string="Demand", required=False, )
    product_uom = fields.Many2one(comodel_name="uom.uom", string="Unit Of Measure", required=False, )

# class StockPicking(models.Model):
#     _inherit='stock.picking'
#
#     def key_func(k):
#         return k['description_bom_line']
#
#
#     def get_kit_lines(self):
#         new_list=[]
#         for line in self.move_lines:
#             new_list.append({
#                 'description_bom_line':line.description_bom_line.id,
#                 'description_bom_line_name':line.description_bom_line.name,
#                 'product_uom_qty':line.product_uom_qty,
#             })
#
#
#         for key, value in groupby(INFO, key_func):
#             print(key)
#             print(list(value))
