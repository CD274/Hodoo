from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'  # Nombre técnico del modelo
    _description = 'Descripción del modelo'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')
