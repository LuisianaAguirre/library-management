from odoo import http
from odoo.http import request
import json

class LibraryManagementController(http.Controller):

    @http.route('/library_management/book/<string:isbn>', type='http', auth='user', methods=['GET'])
    def get_book_by_isbn(self, isbn, **kwargs):
        try:
            # Buscar el libro por ISBN
            book = request.env['library_management.libro'].sudo().search([('isbn', '=', isbn)], limit=1)
            if not book:
                return request.make_response(
                    json.dumps({'error': f'No se encontró un libro con el ISBN {isbn}'}),
                    headers={'Content-Type': 'application/json'},
                    status=404
                )

            # Preparar los datos del libro
            book_data = {
                'id': book.id,
                'title': book.name,
                'author': book.author or '',
                'publication_date': book.publication_date and book.publication_date.isoformat() or None,
                'years_since_publication': book.years_since_publication,
                'isbn': book.isbn,
                'is_available': book.is_available
            }

            # Devolver respuesta JSON
            return request.make_response(
                json.dumps({'status': 'success', 'data': book_data}),
                headers={'Content-Type': 'application/json'}
            )

        except Exception as e:
            return request.make_response(
                json.dumps({'error': str(e)}),
                headers={'Content-Type': 'application/json'},
                status=500
            )