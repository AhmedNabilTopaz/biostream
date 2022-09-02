# Part of AktivSoftware See LICENSE file for full
# copyright and licensing details.
{
    'name': "Tracking Sales Price In Product / Order",

    'summary': """
        Tracking Sales Price In Product / Order""",

    'description': """
        Tracking Sales Price In Product / Order
    """,

    'author': "Ahmed Gaber",
    'license': "AGPL-3",

    'category': 'Sales',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product'],

    # always loaded
    'data': [
        # 'security/price_change_security.xml',
        # 'views/sale_order_view.xml',
    ],

    'installable': True,
}
