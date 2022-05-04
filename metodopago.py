from odoo import models, fields

class ventas(models.Model):
    __name = 'puntoventa.metodopago'

    name = fields.Char(string='Id metodo de pago')
    metodo = fields.Char(string='Metodo de pago')
    
    _sql_constraints = [
        ('unique_metodo', 'unique (name)', 'El metodo de pago ya existe!')
    ]
