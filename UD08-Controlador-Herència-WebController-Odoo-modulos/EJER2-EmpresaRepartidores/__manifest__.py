# -*- coding: utf-8 -*-
{
    'name': "Empresa de Repartos",  # Titulo del módulo
    'summary': "Empresa que gestiona repartos a nivel nacional.",  # Resumen de la funcionaliadad
    'description': """ Empresa de Repartos  """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "David Soriano",
    'website': "",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [

        'security/ir.model.access.csv',
        'views/repartidores.xml',
        'views/vehiculos.xml',
        'views/clientes.xml',
        'views/repartos.xml'
    ]
}
