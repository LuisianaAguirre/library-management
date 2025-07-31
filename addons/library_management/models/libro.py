from odoo import models, fields, api
from datetime import datetime

class Libro(models.Model):
    _name = 'library_management.libro'
    _description = 'Libro de la Biblioteca'

    name = fields.Char(string='Título', required=True)
    author = fields.Char(string='Autor')
    publication_date = fields.Date(string='Fecha de Publicación')
    isbn = fields.Char(string='ISBN', required=True, index=True)
    years_since_publication = fields.Integer(
        string='Años desde Publicación',
        compute='_compute_years_since_publication',
        store=False
    )
    is_available = fields.Boolean(
        string='Disponible',
        compute='_compute_is_available',
        store=False
    )

    @api.depends('publication_date')
    def _compute_years_since_publication(self):
        for record in self:
            if record.publication_date:
                today = datetime.today().date()
                record.years_since_publication = (today - record.publication_date).days // 365
            else:
                record.years_since_publication = 0

    def _compute_is_available(self):
        for record in self:
            active_loans = self.env['library_management.prestamo'].search_count([
                ('libro_id', '=', record.id),
                ('is_returned', '=', False)
            ])
            record.is_available = active_loans == 0