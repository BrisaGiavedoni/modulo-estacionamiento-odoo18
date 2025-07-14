from odoo import models, fields, api

class EstacionamientoCliente(models.Model):
    _name = 'estacionamiento.cliente'
    _description = 'Cliente'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    mensualidad_pagada = fields.Boolean(string="Mensualidad al día", default=False)
    dni = fields.Char(string="DNI")
    email = fields.Char(string="Email")

    movimiento_ids = fields.One2many(
        'vehiculo.movimiento',
        'cliente_id',
        string='Movimientos'
    )

    def action_movimientos(self):
     self.ensure_one()
     return {
        'type': 'ir.actions.act_window',
        'name': 'Movimientos',
        'res_model': 'vehiculo.movimiento',
        'view_mode': 'list,form',
        'domain': [('cliente_id', '=', self.id)],
        'context': {'default_cliente_id': self.id},
        'target': 'new'
       }