from odoo import models, fields

class ventas(models.Model):
    __name = 'puntoventa.ventas'

    name = fields.Char(string='IdVenta')
    
    _sql_constraints = [
        ('unique_categoria', 'unique (name)', 'La categoria ya existe!')
    ]
