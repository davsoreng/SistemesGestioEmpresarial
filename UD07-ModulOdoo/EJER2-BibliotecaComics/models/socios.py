from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Socios(models.Model):
    
    _name = 'socio.biblioteca'
    _description = 'Socios Biblioteca'
    
    _rec_name = 'nombre'

    id = fields.Integer()
    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)

    _sql_contraints = [('id_uniq', 'UNIQUE (id)', 'El "id" es unico')]
    