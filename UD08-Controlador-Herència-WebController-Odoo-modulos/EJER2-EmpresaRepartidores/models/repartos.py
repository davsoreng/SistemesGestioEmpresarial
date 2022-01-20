# -*- coding: utf-8 -*-
from enum import unique
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

#Definimos modelo Repartos, que almacenara información de cada repartidor
class Repartos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'empresa.repartos'

    _description = 'Repartos de la empresa'

    #Parametros de ordenacion por defecto
    _order = 'id'

    #ATRIBUTOS

    #Aqui indicamos que se use el atributo "nombre" como nombre para mostrar
    _rec_name = 'id'

    #Atributo nombre
    id = fields.Integer('Numero de la entrega', readonly=True, )
    repartidor = fields.Many2one('empresa.repartidores', required=True)
    matricula = fields.Many2one('empresa.vehiculos', required=True)
    kilometros = fields.Float('Distancia del trayecto (en KM)', required=True)
    KgPaquete = fields.Float('KG del Paquete', required=True)
    tamanoPaquete = fields.Selection([('pequeno','Pequeno'),('mediano','Mediano'),('grande', 'Grande')],'Tamano del paqueter',default="pequeno")
    observaciones = fields.Html('Observaciones a la hora de la entrega', sanitize=True, strip_style=False)
    estado = fields.Selection([('en preparacion','en preparacion'),('de camino','de camino'),('entregado', 'entregado')],'Estado de la entrega',default="")
    emisor = fields.Char('Empresa emissora', required=True)
    Cliente = fields.Many2one('empresa.clientes',required=True)
    fechaActual = fields.Date(string="Fecha actual", default=datetime.today(), readonly=True)
    fechaInicio = fields.Datetime(string="Fecha inicio", required=True)
    fechaRetorno = fields.Datetime(string="Hora de vuelta del reparto", required=True)
    fechaEntrega = fields.Datetime(string="Hora de la entrega del paquete")

    _sql_constraints = [('id', 'UNIQUE (id)', 'El "id" es unico')]

    @api.constrains('repartidor')
    def can_travel(self):
        for record in self:
            if record.repartidor.tieneCarnet == False:
                raise models.ValidationError('No se puede crear el reparto si el repartidor no tiene carnet')
            
            if self.repartidor in record.repartidor and record.estado == "de camino":
                raise models.ValidationError('El repartidor está en reparto')

    @api.constrains('kilometros')
    def distance(self):
        for record in self:
            if record.kilometros > 10.00 and record.matricula.tipoDeVehiculo == "bicicleta":
                raise models.ValidationError('La bicicleta no puede recorrer mas de 10Km')
            if record.kilometros < 1.00 and record.matricula.tipoDeVehiculo == "furgoneta":
                raise models.ValidationError('La fungoneta tiene que hacer un recorrido minimode 1Km')