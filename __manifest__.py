# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    'name': 'Rawaj POS Custom Receipt',
    'category': 'Sales/Point of Sale',
    'summary': 'This module is used to customized receipt of point of sale to meet Rawaj design',
    'description': "Rawaj receipt",
    'version': '16.0.1.0',
    'author': 'Ahmed yahia',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            # "rawaj_receipt/static/src/js/models.js",
            "rawaj_receipt/static/src/xml/pos.xml",
        ],
    },
    'installable': True,
}
