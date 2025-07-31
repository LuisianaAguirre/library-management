Library Management – Odoo 18
Sistema de gestión de biblioteca desarrollado como parte de una prueba técnica funcional para pasantía. Incluye administración de socios, catálogo de libros, gestión de préstamos, y un servicio REST.
-----------------------------------------------
Requisitos Previos:
Docker
Docker Compose
-----------------------------------------------

Instalación:

Clonar el repositorio: 
git clone https://github.com/tu-usuario/library-management.git
cd library-management

Levantar el entorno Docker: docker-compose up -d

Acceder a Odoo: http://localhost:8069

Crear una nueva base de datos, con contraseña admininistrador: luisiana14
Puede modificar esta contraseña editando el archivo odoo.conf, línea: admin_passwd = luisiana14

Instalar el módulo "Library Management"

----------------------------------------------- 
Funcionalidades:

1. Módulo principal
Módulo library_management agrupando todas las funcionalidades.

2. Gestión de miembros
Alta de socios con nombre, fecha de alta y código de socio único generado automáticamente.

3. Catálogo de libros
Registro de libros con ISBN, título, autor y fecha de publicación.

Cálculo automático de la antigüedad del libro (años desde publicación).

4. Préstamos de libros
Registro de préstamos por socio (máximo 5 simultáneos).

Registro manual de devoluciones.

5. Servicio REST externo
Endpoint: /api/book/<isbn>
Devuelve información JSON del libro: disponibilidad y su identificador interno.

http://localhost:8069/library_management/book/<isbn>

Ejemplo de respuesta
json
{
  "status": "success",
  "data": {
    "id": 1,
    "title": "Prueba",
    "author": "Autor Ejemplo",
    "publication_date": "2020-01-01",
    "years_since_publication": 5,
    "isbn": "1234567890",
    "is_available": true
  }
}