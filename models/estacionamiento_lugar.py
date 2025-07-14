from odoo import fields, models, api
from odoo.exceptions import ValidationError

class EstacionamientoLugar(models.Model):
    _name = "estacionamiento.lugar"
    _description = "Lugar de Estacionamiento"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre", required=True)
    estado = fields.Selection(
        [('Libre', 'Libre'), ('Ocupado', 'Ocupado')],
        string="Estado",
        default='Libre',
        readonly=True
    )

    @api.constrains('nombre')
    def _check_nombre_unico(self):
     for rec in self:
        otros = self.search([
            ('nombre', '=', rec.nombre),
            ('id', '!=', rec.id)
        ])
        if otros:
            raise ValidationError("Ya existe un lugar con ese nombre.")