from odoo import models, fields, api

class EstacionamientoEstado(models.Model):
    _name = 'estacionamiento.estado'
    _description = 'Resumen de ocupación'

    nombre = fields.Char(default="Estado general", readonly=True)
    total_lugares = fields.Integer(string="Total de Lugares", compute="_compute_ocupacion", store=False)
    lugares_ocupados = fields.Integer(string="Lugares Ocupados", compute="_compute_ocupacion", store=False)
    lugares_libres = fields.Integer(string="Lugares Libres", compute="_compute_ocupacion")

    @api.depends()
    def _compute_ocupacion(self):
        Lugar = self.env['estacionamiento.lugar']
        total = Lugar.search_count([])
        ocupados = Lugar.search_count([('estado', '=', 'Ocupado')])
        for rec in self:
            rec.total_lugares = total
            rec.lugares_ocupados = ocupados
            rec.lugares_libres = total - ocupados
