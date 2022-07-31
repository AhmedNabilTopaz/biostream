# -*- coding: utf-8 -*-
{
    'name': "Bio stream Sales Rep",

    'summary': """
        Sales Re""",

    'description': """
        Sales Re
    """,

    'author': "Ahmed Gaber",

    'category': 'sale',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','sale','calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sales_rep_view.xml',
        'views/sale_view.xml',

    ],
    # only loaded in demonstration mode

}
