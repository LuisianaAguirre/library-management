from odoo import models, fields, api
import uuid

class Socio(models.Model):
    _name = 'library_management.socio'  # Correcto, pero el prefijo debería coincidir con el nombre del módulo
    _description = 'Socio de la biblioteca'

    name = fields.Char(string='Nombre', required=True)
    start_date = fields.Date(string='Fecha de Alta', default=fields.Date.today)
    member_code = fields.Char(string='Código de Socio', readonly=True, copy=False)

    @api.model
    def create(self, vals):
        vals['member_code'] = str(uuid.uuid4())[:8]  # Genera un código único de 8 caracteres
        return super(Socio, self).create(vals)