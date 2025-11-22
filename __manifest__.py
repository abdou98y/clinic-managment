# -*- coding: utf-8 -*-
{
    'name': 'Clinic Management System',
    'version': '18.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'Comprehensive clinic management system for patient care, vital signs, and prescriptions',
    'description': """
Clinic Management System
========================

A comprehensive healthcare management solution built for Odoo 18 Community Edition.

Key Features:
* Patient Profile Management with medical history
* Vital Signs Recording with automatic BMI calculation
* Medication Database with drug interaction checking
* Prescription Management with printable reports
* Security and access controls for healthcare data
* HIPAA compliance features and audit trails

This module provides healthcare facilities with a complete solution for managing
patient care workflows from registration through diagnosis and treatment.
    """,
    'author': 'Abdelrhman younes',
    'website': 'https://github.com/abdou98y/clinic-managment',
    'license': '',
    'depends': [
        'base',
        'mail',
        'web',
        'portal',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Reports
        'report/clinic_patient_report.xml',
        'report/report_medical_prescription.xml',
        'report/report_medical_prescription_action.xml',
        # Data
        'data/clinic_sequence.xml',
        # Views
        'views/clinic_patient_views.xml',
        'views/clinic_vital_signs_views.xml',
        'views/lap_result.xml',
        'views/clinic_menu.xml',
        'views/patient_complaint.xml',
        'views/prescription.xml',
        # Wizards
    ],
    'assets': {
        'web.assets_backend': [
            'clinic_management/static/src/css/clinic_management.css',
            'clinic_management/static/src/js/clinic_management.js',
        ],
        'web.assets_frontend': [
            'clinic_management/static/src/css/clinic_portal.css',
        ],
        'web.report_assets_common': [
                'clinic_management/static/src/scss/fonts.scss',
            ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['reportlab', 'qrcode'],
    },
}

