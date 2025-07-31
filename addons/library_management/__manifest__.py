{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Gestionar socios, libros y préstamos de biblioteca', 
    'category': 'Services/Library',
    'author': 'Luisiana A.',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/socio_views.xml',
        'views/libro_views.xml',
        'views/prestamo_views.xml',
    ],
    'controllers': [
        'controllers/library_management.py',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
