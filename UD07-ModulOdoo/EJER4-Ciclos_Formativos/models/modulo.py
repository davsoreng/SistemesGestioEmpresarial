# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Modulo(models.Model):

    _name = 'modulo'
    _description = 'Modulo'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    alumnos = fields.Many2many('alumno', required=True)
    profesor = fields.Many2one('profesor', required=True)
    