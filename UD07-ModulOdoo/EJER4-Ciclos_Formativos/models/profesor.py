# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Profesor(models.Model):

    _name = 'profesor'
    _description = 'Profesores'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True, index=True)
    apellido = fields.Char('Apellido', required=True, index=True)
    id = fields.Integer('ID PROFESOR')

    _sql_constraints = [('id', 'UNIQUE (id)', 'El "id" debe ser unico')]