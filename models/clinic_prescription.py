from odoo import models, fields, api

class Prescription(models.Model):
    _name = "medical.prescription"
    _description = "Prescription"

    name = fields.Char()
    main_complaint_id = fields.Many2one(
        "main.complaint",
        string="Main Complaint",
        ondelete="restrict",
        required=True,
        default=lambda self: self._get_default_main_complaint_id(),
    )



    treatment_line_ids = fields.One2many(
        'medical.prescription.line',
        'prescription_id',
        string="Treatments"
    )
    patient_id = fields.Many2one(
        'clinic.patient',
        related='main_complaint_id.patient_id',
        store=True,
        string="Patient"
    )

    def _get_default_main_complaint_id(self):
        patient_id = self.env.context.get("default_patient_id")

        if not patient_id:
            return False
        last_complaint = self.env['main.complaint'].search(
            [('patient_id', '=', patient_id)],
            order="id desc",
            limit=1
        )
        return last_complaint.id if last_complaint else False



    @api.model
    def create(self, vals):
        """Automatically link to latest main complaint of the patient."""
        if not vals.get('main_complaint_id') and vals.get('patient_id'):
            latest = self.env['main.complaint'].search(
                [('patient_id', '=', vals['patient_id'])],
                order='create_date desc',
                limit=1
            )
            if latest:
                vals['main_complaint_id'] = latest.id
        return super().create(vals)

    def name_get(self):
        result = []
        for rec in self:
            if rec.main_complaint_id:
                name = f"{rec.main_complaint_id.display_name} - Prescription"
            else:
                name = "New Prescription"
            result.append((rec.id, name))
        return result

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        patient_id = self.env.context.get('default_patient_id')
        if patient_id and 'main_complaint_id' in fields_list:
            latest = self.env['main.complaint'].search(
                [('patient_id', '=', patient_id)],
                order='date desc',
                limit=1
            )
            if latest:
                defaults['main_complaint_id'] = latest.id
        return defaults

    def action_print_prescription(self):
        """Return HTML report for browser printing"""
        return self.env.ref('clinic_management.report_medical_prescription').report_action(self, data={'id': self.id})
