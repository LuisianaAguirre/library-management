from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Prestamo(models.Model):
    _name = 'library_management.prestamo'
    _description = 'Préstamo de la Biblioteca'

    socio_id = fields.Many2one('library_management.socio', string='Socio', required=True)
    libro_id = fields.Many2one('library_management.libro', string='Libro', required=True)
    fecha_prestamo = fields.Date(string='Fecha de Préstamo', default=fields.Date.today, required=True)
    is_returned = fields.Boolean(string='Marcar Devolución', default=False, help="Marcar para indicar que el libro ha sido devuelto")
    estado_display = fields.Char(
        string='Estado',
        compute='_compute_estado_display',
        store=False
    )

    @api.depends('is_returned')
    def _compute_estado_display(self):
        for record in self:
            record.estado_display = 'Devuelto' if record.is_returned else 'Activo'

    @api.constrains('socio_id', 'is_returned')
    def _check_max_loans(self):
        for record in self:
            if not record.is_returned:
                active_loans = self.search_count([
                    ('socio_id', '=', record.socio_id.id),
                    ('is_returned', '=', False)
                ])
                if active_loans > 5:
                    raise ValidationError(
                        f"El socio {record.socio_id.name} ya tiene 5 préstamos activos. "
                        "Para liberar cupo, es necesario devolver un libro."
                    )