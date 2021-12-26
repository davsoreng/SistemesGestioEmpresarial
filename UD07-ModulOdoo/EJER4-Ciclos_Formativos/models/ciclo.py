# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Ciclo(models.Model):

    _name = 'ciclo'
    _description = 'Ciclos del Instituto'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    modulo = fields.Many2many('modulo', required=True)
    