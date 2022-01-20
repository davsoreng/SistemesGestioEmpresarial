# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos modelo Clientes, que almacenara información de cada repartidor
class Clientes(models.Model):

    #Nombre y descripcion del modelo
    _name = 'empresa.clientes'

    _description = 'Clientes de la empresa'

    #Parametros de ordenacion por defecto
    _order = 'nombre'

    #ATRIBUTOS

    #Aqui indicamos que se use el atributo "nombre" como nombre para mostrar
    _rec_name = 'nombre'

    #Atributo nombre
    nombre = fields.Char('Nombre Cliente', required=True, index=True)
    apellido = fields.Char('Apellido Cliente', required=True, index=True)
    dni = fields.Integer('DNI Cliente', required=True, index=True)
    telefono = fields.Integer('Telefono', required=True, index=True)

    _sql_contraints = [('dni_unique', 'UNIQUE (dni)', 'El dni es unico')]