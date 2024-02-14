
{
    'name': 'Price surchage',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_view.xml',
        'views/surcharge_mapping.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
