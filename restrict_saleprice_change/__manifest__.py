# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.
{
    'name': "Sale Price Change Restriction",

    'summary': """
        Restrict price change on orders""",

    'description': """
        Restrict price change on orders
    """,

    'author': "Ahmed Gaber",
    'license': "AGPL-3",

    'category': 'Sales',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'security/price_change_security.xml',
        'views/sale_order_view.xml',
    ],

    'installable': True,
}
