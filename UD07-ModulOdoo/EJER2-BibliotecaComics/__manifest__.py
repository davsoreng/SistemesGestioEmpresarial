# -*- coding: utf-8 -*-
{
    'name': "Biblioteca Comics Simple",  # Titulo del módulo
    'summary': "Gestionar comics :) (Version simple)",  # Resumen de la funcionaliadad
    'description': """
Gestor de bibliotecas (Version Simple)
==============
    """,  

    'application': True,
    'author': "David SOriano",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_comic.xml',
        'views/socios.xml',
        'views/prestamos.xml'
    ],
}
