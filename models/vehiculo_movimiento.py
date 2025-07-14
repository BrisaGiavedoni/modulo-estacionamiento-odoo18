from odoo import api, fields, models
from odoo.exceptions import ValidationError # Correcto
from datetime import timedelta

class EstacionamientoMovimiento(models.Model):
    _name = "vehiculo.movimiento"
    _description = "Movimiento de Vehículos"
    _order = "fecha_entrada desc"

    cliente_id = fields.Many2one(
        'estacionamiento.cliente',
        string='Cliente',
        required=True
    )

    vehiculo_id = fields.Many2one(
        comodel_name="estacionamiento.vehiculo",
        string='Vehículo',
        required=True
    )

    lugar_id = fields.Many2one(
        comodel_name="estacionamiento.lugar",
        string="Lugar de estacionamiento",
        domain="[('estado', '=', 'Libre')]",
        required=True
    )

    fecha_entrada = fields.Datetime(
        string="Fecha de entrada",
        default=fields.Datetime.now
    )

    duracion = fields.Selection([
        ('15', '15 días'),
        ('30', '1 mes')
    ], default='30', string="Duración")

    fecha_salida = fields.Datetime(
        string="Fecha de salida",
        compute='_compute_fecha_salida',
        store=True
    )

    @api.onchange('vehiculo_id')
    def _onchange_vehiculo_id(self):
        if self.vehiculo_id and self.vehiculo_id.cliente_id:
            self.cliente_id = self.vehiculo_id.cliente_id

    @api.depends('fecha_entrada', 'duracion')
    def _compute_fecha_salida(self):
        for rec in self:
            if rec.fecha_entrada:
                dias = 15 if rec.duracion == '15' else 30
                rec.fecha_salida = rec.fecha_entrada + timedelta(days=dias)

    @api.constrains('fecha_entrada', 'fecha_salida')
    def _check_fechas(self):
        for rec in self:
            if rec.fecha_entrada and rec.fecha_salida:
                if rec.fecha_salida < rec.fecha_entrada:
                    raise ValidationError("La salida no puede ser antes que la entrada.")

    @api.constrains('vehiculo_id')
    def _check_vehiculo_ya_estacionado(self):
        for rec in self:
            existe = self.search_count([
                ('vehiculo_id', '=', rec.vehiculo_id.id),
                ('id', '!=', rec.id),
                ('fecha_salida', '>', fields.Datetime.now())
            ])
            if existe:
                raise ValidationError("Este vehículo ya está estacionado actualmente.") 

    @api.model_create_multi
    def create(self, vals_list):
        movimientos = super().create(vals_list)
        for movimiento in movimientos:

            if movimiento.lugar_id.estado != 'Libre':
                raise ValidationError("El lugar seleccionado ya está ocupado.") 

            if not movimiento.vehiculo_id.cliente_id.mensualidad_pagada:
                raise ValidationError( 
                    f"El cliente del vehículo {movimiento.vehiculo_id.patente} no tiene la mensualidad paga."
                )

            movimiento.lugar_id.estado = 'Ocupado'

        return movimientos

    def registrar_salida(self):
        for rec in self:
            
            rec.fecha_salida = fields.Datetime.now()
            rec.lugar_id.estado = 'Libre'

    @api.constrains('vehiculo_id')
    def _check_mensualidad_pagada(self):
       for rec in self:
         if not rec.vehiculo_id.cliente_id.mensualidad_pagada:
             raise ValidationError("El cliente no tiene la mensualidad al día.")