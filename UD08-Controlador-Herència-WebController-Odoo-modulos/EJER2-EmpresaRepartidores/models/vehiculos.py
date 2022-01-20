# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Definimos modelo Repartidores, que almacenara información de cada repartidor
class Vehiculos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'empresa.vehiculos'

    _description = 'Vehiculos de la empresa'

    #Parametros de ordenacion por defecto
    _order = 'matricula'

    #ATRIBUTOS

    #Aqui indicamos que se use el atributo "nombre" como nombre para mostrar
    _rec_name = 'matricula'

    #Atributo nombre
    matricula = fields.Integer('Matricula del vehículo', required=True, index=True)
    tipoDeVehiculo = fields.Selection([('ninguno','Ninguno'),('furgoneta','Furgoneta'),('bicicleta', 'Bicicleta')],'Tipo de vehiculo',default="ninguno")

    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen)
    foto = fields.Image('Foto del vehiculo',max_width=50,max_height=50)

    #Una breve descripcion sobre las caracteristicas visuales del veh
    descripcion = fields.Html('Descripción breve del vehiculo', sanitize=True, strip_style=False)

    _sql_contraints = [('matricula_uniq', 'UNIQUE (matricula)', 'La matricula es unica')]
