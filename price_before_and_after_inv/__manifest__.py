# -*- coding: utf-8 -*-
{
    'name': "Inv Price before After",

    'summary': """
        Inv Price before After""",

    'description': """
        Inv Price before After
    """,

    'author': "Ahmed Gaber",
    'category': 'Accounting',

    'license': 'LGPL-3',
    'currency': 'EUR',
    'depends': ['base', 'account','sale' ],


    'data': [
        'views/ks_account_invoice.xml',
        'views/report_invoice.xml',

    ],

}
