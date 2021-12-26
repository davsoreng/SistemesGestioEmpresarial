# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Alumno(models.Model):

    _name = 'alumno'
    _description = 'Alumnos'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)
    id = fields.Integer('NIE')

    _sql_constraints = [('id', 'UNIQUE (id)', 'El "id" debe ser unico')]
