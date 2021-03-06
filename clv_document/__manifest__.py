# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Document',
    'summary': 'Document Module used by CLVsol Solutions.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_global_log',
        'clv_global_tag',
    ],
    'data': [
        'security/document_security.xml',
        'security/ir.model.access.csv',
        'views/document_view.xml',
        'views/document_log_view.xml',
        'views/document_category_view.xml',
        'views/document_category_log_view.xml',
        'views/global_tag_view.xml',
        'views/document_type_view.xml',
        'views/document_type_log_view.xml',
        'views/document_item_view.xml',
        'views/referenceable_model_view.xml',
        # 'data/document_mass_editing.xml',
        'wizard/document_mass_edit_view.xml',
        'wizard/document_items_refresh_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
