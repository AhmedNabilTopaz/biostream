# Copyright © 2019 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# @author: Iryna Razumovska (<support@garazd.biz>)
# License OPL-1 (https://www.odoo.com/documentation/14.0/legal/licenses.html#odoo-apps).

{
    'name': 'eCommerce Facebook Pixel | Meta Pixel',
    'version': '15.0.1.0.1',
    'category': 'eCommerce',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'license': 'OPL-1',
    'summary': 'eCommerce Facebook (Meta) Pixel | Track Events | Integration | Add eCommerce events to product and category website pages',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'live_test_url': 'https://apps.garazd.biz/r/Uiw',
    'depends': [
        'website_sale',
        'website_facebook_pixel',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/website_sale_templates.xml',
    ],
    'external_dependencies': {
    },
    'price': 65.0,
    'currency': 'EUR',
    'support': 'support@garazd.biz',
    'application': True,
    'installable': True,
    'auto_install': False,
}
