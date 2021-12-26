from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pacientes(models.Model):
    
    _name = 'paciente'
    _description = 'Pacientes Hospital'
    
    _rec_name = 'nombre'

    id = fields.Integer()
    nombre = fields.Char('Nombre', required=True, index=True)
    apellido = fields.Char('Apellido', required=True)
    sintomas = fields.Html('Sintomas', sanitize=True, strip_style=False)

    _sql_contraints = [('id_uniq', 'UNIQUE (id)', 'El "id" es unico')]
    