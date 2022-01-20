# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos modelo Repartidores, que almacenara información de cada repartidor
class Repartidores(models.Model):

    #Nombre y descripcion del modelo
    _name = 'empresa.repartidores'

    _description = 'Repartidores de la empresa'

    #Parametros de ordenacion por defecto
    _order = 'nombre'

    #ATRIBUTOS

    #Aqui indicamos que se use el atributo "nombre" como nombre para mostrar
    _rec_name = 'nombre'

    #Atributo nombre
    nombre = fields.Char('Nombre Repartidor', required=True, index=True)
    apellido = fields.Char('Apellido Repartidor', required=True, index=True)
    dni = fields.Integer('DNI Repartidor', required=True, index=True)
    telefono = fields.Integer('Telefono', required=True, index=True)

    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen)
    foto = fields.Image('Foto del repartidor',max_width=50,max_height=50)

    #Dato del carnet, queremos saber si tiene o no carnet de conducir
    tieneCarnet = fields.Boolean('¿Tiene carnet?', Required=True)

    tipoCarnet = fields.Selection([('ninguno','Ninguno'),('furgoneta','Furgoneta'),('ciclomotor', 'Ciclomotor')],'Tipo de Carnet',default="ninguno")

    _sql_contraints = [('dni_unique', 'UNIQUE (dni)', 'El dni es unico')]

