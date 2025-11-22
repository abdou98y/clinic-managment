from odoo import models, fields, api

class PrescriptionLine(models.Model):
    _name = "medical.prescription.line"
    _description = "Prescription Line"

    prescription_id = fields.Many2one('medical.prescription', string="Prescription", ondelete="cascade")
    treatment_id = fields.Many2one('medical.treatment', string="Treatment")
    treatment_name = fields.Char(string="Treatment Name (if new)")
    usage_ar = fields.Text(related='treatment_id.usage_ar', string="Usage (Arabic)", readonly=False)


