from odoo import api, fields, models

class EstacionamientoVehiculo(models.Model):
    _name = "estacionamiento.vehiculo"
    _description = "Vehículo"
    _rec_name = 'patente'

    patente = fields.Char(string="Patente", required=True)
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    cliente_id = fields.Many2one(
        comodel_name='estacionamiento.cliente',
        string="Cliente",
        required=True
    )
    _sql_constraints = [
        ('unique_patente', 'unique(patente)', 'La patente debe ser única.')
    ]