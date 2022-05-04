from odoo import models, fields

class detalleventas(models.Model):
    __name = 'puntoventa.categoria'

    name = fields.Many2one('puntoventa.venta',string='Id venta')
    producto = fields.Many2one('puntoventa.producto',string='Categoria')
    cantidad = fields.Integer(string='Cantidad')
    
    
    _sql_constraints = [
        ('unique_detalleventa', 'unique (name)', 'El detalle de la venta ya existe!')
    ]
