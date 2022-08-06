# -*- coding: utf-8 -*-

{
    'name': "BioStream VIP Access Rights",
    'author': 'Ahmed Gaber',
    'category': 'Sales',
    'summary': """BioStream VIP Access Rights""",
    'description': """
    1- Hide Sale Price of the Product
    2- Hide Cost Price of the Product
    3- partner creation restiction
    """,
    'version': '15.0',
    'depends': ['account', 'purchase', 'base', 'sales_team', 'mrp', 'stock', 'sale', ],
    'data': [
        'security/show_sale_cost_price_fields.xml',
        'security/ir.model.access.csv',
        'views/view_sale_cost_price_product.xml',

    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
