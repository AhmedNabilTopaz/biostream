# -*- encoding: utf-8 -*-

##############################################################################
{
    'name': "Invoice City State",
    'version': '13.0',
    'summary': """
        Invoice City State""",

    'description': """
        Invoice City State
    """,

    'author': "Ahmed Gaber",
    'category': 'Others',
    'version': '0.1',
    'depends': ['base', 'account','sale'],
    'data': [

        'views/sale_view.xml',
        'views/invoice_view.xml',
        'views/sale_invoice_report.xml',

    ],

}
