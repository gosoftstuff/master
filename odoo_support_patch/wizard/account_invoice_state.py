# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import UserError


class AccountInvoiceConfirm(models.TransientModel):
    """
    This wizard will confirm the all the selected draft invoices
    """

    _inherit = "account.invoice.confirm"

    @api.multi
    def invoice_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['account.invoice'].browse(active_ids):
            if record.state not in ('draft', 'proforma', 'proforma2'):
                raise UserError(_("Selected invoice(s) cannot be confirmed as they are not in 'Draft' or 'Pro-Forma' state."))
            # commit the transaction after each sales order / invoice is validated,
            # so the lock is released after each sales order / invoice.
            # For instance, for the invoice validation, creating a module overriding
            # record.action_invoice_open()
            try:
                record.action_invoice_open()
                record.env.cr.commit()
            except Exception:
                continue
        return {'type': 'ir.actions.act_window_close'}

