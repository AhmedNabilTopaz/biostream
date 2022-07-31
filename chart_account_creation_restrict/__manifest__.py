# -*- coding: utf-8 -*-

{
    'name': "Chart Account Creation Restriction",
    'summary': """Chart Account Creation Restriction""",
    'description': """Chart Account Creation Restriction.""",
    'author': "Ahmed Gaber",
    'license': 'AGPL-3',
    'category': 'base',
    'version': '13.0',
    'depends': ['account','base',],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/account_move_view.xml',
    ],
    "images": [
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
