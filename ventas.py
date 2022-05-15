
from odoo import models, fields, api

class ventas(models.Model):
    _name = 'puntoventa.ventas'

    name = fields.Char(string='IdVenta')
   
    detalleventas = fields.One2many('puntoventa.detalleventa','name', string='Detalles')
    total=fields.Integer(tring='Total')
    
    _sql_constraints = [
        ('unique_categoria', 'unique (name)', 'La venta ya existe!')
    ]

    @api.depends('detalleventas')
    def calcularTotal(self):
        acumulado = 0 
        for c in self.detalleventas:
            acumulado += c.precio * c.cantidad 
        if len(self.detalleventas) != 0:
            self.total=acumulado
        else:
            self.total=0


class detalleventas(models.Model):
    _name = 'puntoventa.detalleventa'

    _rec_name='producto'
    name = fields.Many2one('puntoventa.ventas',string='Venta', store='True')
    producto = fields.Many2one('puntoventa.producto',string = 'Producto')
    precio = fields.Integer(string = 'Precio unitario', related='producto.precio', store='True')
    cantidad = fields.Integer(string ='Cantidad')
    
    _sql_constraints = [
        ('unique_detalleventa', 'unique (name)', 'El detalle de la venta ya existe!')
    ]

   
