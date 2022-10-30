# -*- coding: utf-8 -*-
{
    'name': "custom_login",
    'description': """Remove *Manage Databases* and *Powered by Odoo* at the bottom of the login page""",
    'author': "DERICK TEMFACK",
    'website': "https://github.com/tderick/custom-odoo-login",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': False,
    'installable': True,
    'auto_install': True,
    'licence': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/login_layout_template.xml',
    ],
    "qweb": ["static/src/xml/base.xml"]

}
