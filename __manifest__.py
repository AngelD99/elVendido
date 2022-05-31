# -*- coding: utf-8 -*-
{
    'name': 'elvendido',
    'version': '1.0',
    'category': 'ventas',
    'description': 'punto de venta',
    'author': 'De la Rosa Nuniez Brayan, Sanchez Magania Joan Patrick, Valdovinos Sanchez Miguel Angel, Zamora Magadan Jose Alejandro',
    'maintainer': 'ITSA',
    'website': 'http://www.itsa.edu.mx',
    'depends': ['base'],
    'data': [
        'security/grupos.xml',
        'security/ir.model.access.csv',
        'reports/ticket.xml',
        'views/categoria_view.xml',
        'views/metodopago_view.xml',
        'views/producto_view.xml',
        'views/ventas_view.xml',
        'views/menu_view.xml',        
    ],
    'installable': True,
    'auto_install': False,
}