# -*- coding: utf-8 -*-
{
    'name': "Hospital",
    'summary': "Hosptial",
    'description': "Diagnosticar Problemas de Pacientes.",
    'author': "David Soriano",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/diagnosticos.xml',
        'views/pacientes.xml',
        'views/medicos.xml'
    ]
}
