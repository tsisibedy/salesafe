# -*- coding: utf-8 -*-
{
    'name': "SaleSafe",
    'icon': '/salesafe/static/src/img/salesafe.png',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "SaleSafe est une application pour vous aider a vendre votre produit en toute securité en etant aucourent de toute action de votre vente, cree par cenoel",

    'author': "cenoel",
    'website': "trazafimiandrisoa@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board','website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/print_received.xml',
        'views/main.xml',
        'views/product.xml',
        'views/update_product.xml',
        'views/sale.xml',
        'views/sale_service.xml',
        'views/promotion.xml',
        'views/history.xml',
        'views/board.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/content.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
