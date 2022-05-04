from odoo import models, fields

class categoria(models.Model):
    __name = 'puntoventa.categoria'

    name = fields.Char(string='IdCategoria')
    categoria = fields.Char(string='Categoria')
    
    
    _sql_constraints = [
        ('unique_categoria', 'unique (name)', 'La categoria ya existe!')
    ]
