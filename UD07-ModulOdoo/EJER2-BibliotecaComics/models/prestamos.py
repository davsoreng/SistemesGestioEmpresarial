from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class BibliotecaPrestamo(models.Model):

    _name = 'prestamo.biblioteca'
    _description = 'Prestamos de la biblioteca'

    comic = fields.Many2one('biblioteca.comic', required=True)
    socio = fields.Many2one('socio.biblioteca', required=True)
    
    inicio_fecha = fields.Date('Inicio Prestamo')
    fin_fecha = fields.Date('Fin Prestamo')

    _sql_constraints = [
        ('comic_uniq', 'UNIQUE (comic)', 'El comic es unico')
    ]
    
    @api.constrains('inicio_fecha','fin_fecha')
    def _fecha(self):
        for record in self:
            fechaActual = date.today()
            fechaInicio = record.inicio_fecha
            if(fechaInicio):
                if(fechaInicio > fechaActual):
                    raise ValidationError("ERROR! La fecha de Inicio debe ser hoy o anterior")
            fechaFin = record.fin_fecha
            if(fechaFin):
                if(fechaFin < fechaActual):
                    raise ValidationError("ERROR! La fecha de Fin debe ser hoy o posterior")