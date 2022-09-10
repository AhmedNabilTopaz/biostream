# -*- coding: utf-8 -*-
{
    'name': "Bio stream Medical Rep",

    'summary': """
        Medical Rep""",

    'description': """
        Medical Rep
    """,

    'author': "Ahmed Gaber",

    'category': 'sale',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','sale','calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/medical_rep_view.xml',
        'views/partner_view.xml',
        'views/sale_view.xml',

    ],
    # only loaded in demonstration mode

}
