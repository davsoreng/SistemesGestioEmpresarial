from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Medicos(models.Model):

    _name = 'medico'
    
    _description = 'Medicos de la Hospital'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    apellido_uno = fields.Char('Primer Apellido', required=True)
    apellido_dos = fields.Char('Segundo Apellido', required=True)
    numero_colegiado = fields.Integer('Nº Colegiado' , required=True)

    _sql_constraints = [('numero_colegiado_uniq', 'UNIQUE (numero_colegiado)', 'El numero_colegiado es unico')]