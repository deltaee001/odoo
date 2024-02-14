
{
    'name': 'Price surchage',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/surcharge_mapping.xml'
    ],
    'installable': True,
    'auto_install': False,
}
