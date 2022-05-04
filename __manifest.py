# -*- coding: utf-8 -*-
{
    'name': 'puntoventa',
    'version': '1.0',
    'category': 'ventas',
    'description': 'punto de venta',
    'author': 'De la Rosa Nuniez Brayan, Sanchez Magania Joan Patrick, Valdovinos Sanchez Miguel Angel, Zamora Magadan Jose Alejandro',
    'maintainer': 'ITSA',
    'website': 'http://www.itsa.edu.mx',
    'depends': ['base'],
    'data': [
        'views/categoria_view.xml',
        'views/detalleventa_view.xml',
        'views/metodopago_view.xml',
        'views/producto_view.xml',
        'views/ventas_view.xml',
        'reports/kardex.xml',
        'views/menu_view.xml',
        
    ],
    'installable': True,
    'auto_install': False,
}