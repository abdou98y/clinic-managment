from odoo import models, fields, api

class Treatment(models.Model):
    _name = "medical.treatment"
    _description = "Treatment"

    name = fields.Char(string="Treatment (English)", required=True, translate=True)
    usage_ar = fields.Text(string="Usage (Arabic)", translate=True)

    _sql_constraints = [
        ('unique_treatment_name', 'unique(name)', 'This treatment already exists!')
    ]
