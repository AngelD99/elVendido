from odoo import models, fields

class producto(models.Model):
    __name = 'puntoventa.producto'

    name = fields.Char(string='IdProducto')
    producto = fields.Char(string='Nombre del producto')
    categoria = fields.Many2one('puntoventa.categoria', string='Categoria')
    precio = fields.Integer(string='Precio')
    cantidad = fields.Integer(string='Cantidad disponible')
    

    _sql_constraints = [
        ('unique_categoria', 'unique (name)', 'La categoria ya existe!')
    ]
