# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Diagnosticos(models.Model):

    _name = 'diagnostico'

    _description = 'Diagnosticos del Hospital'

    _rec_name = 'id'

    id = fields.Integer()
    paciente = fields.Many2one('paciente', required=True)
    medico = fields.Many2one('medico', required=True)
    descripcion = fields.Html('Diagnostico', sanitize=True, strip_style=False)

    _sql_constraints = [('id_uniq', 'UNIQUE (id)', 'El "id" debe ser único')]


