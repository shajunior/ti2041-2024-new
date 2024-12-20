<<<<<<< HEAD
# ti2041-2024-new
Repositorio curso Back_end
=======
Hola Profesor Andre le presento mi READ.ME de mi proyecto como solicitado en el cual explica el desarrollo de 
mi Aplicacion que tiene por nombre Gestion_producto asi que ahora voy empezar a explicar todos los pasos que realice para 
alcanzar lograr crear mi aplicacion entonces en primer lugar que hice fue verificar si tengo python instalado con el siguiente comando
 python --version me salio que tengo la version 3.10 ,ya habia tenido django instaldo desde en las clases interiormente asi que pase
 directo a crear mi proyecto de la siguiente manera ;django -admin startproyect Gestion_producto ,para ejecutar mi proyecto escribi 
 el siguiente comando python manage.py runserver y se me creo el proyecto con las siguientes
 carpetas ;__pycache__,__init__.py,asgi.py,settings.py,ulrs.py,wsgi.py luego pase a crear mi aplicacion asi con el comando 
 python manage.py startapp Productos se me creo mi aplicacion dentro productos se genero siguientes archivos ;__pucache__,migrations,
 __init__.py, admin.py, apps.py, models.py, test.py, urls.py, views.py, db.sqlite3 y manage.py ,luego empece a configurar mi aplicacion 
 como fue menciono en la pauta de la evaluacion para eso enfoque en el objectivo principal era crear una aplicacion basica en django para
 para una empreza que quiere gestion su producto que cuenta la aplicacion un registro de producto ,un crear producto y consulta producto
 para eso lo que hice fue crear la ruta de mi aplicacion en URLS.PY y la ruta padre de mi aplicacion en settings.py y views donde esta lo 
 que quiero que el usuario vea en el navegador y luego crear mi templates donde se encuentran consulta.html,registro.html y resulatado.html,y Utiliza archivos CSS para estilizar las pantallas de la aplicación, asegurando una presentación coherente y profesional,para 
 eso crei una carpeta static dentro se encuentra mi estilo.css para poder ejecutar mi aplicacion se necesita seguir esos pasos ,primero colocar cd evaluaciones y dir para ver que hay dentro evaluaciones va aparacer sumativa1 y dir para ver lo que hay dentro de sumativa1 ahi va encontrar mi proyecto Gestion_producto luego cd para acceder a gestion_producto y dir va aparecer mis archivos manage.py y ahi se colocar python manage.py runserver se genero el puerto http://127.0.0.1:8000/ pero la ruta principal es http://127.0.0.1:8000/productos.
 eso se fue todo gracias hasta pronto Profesor Andres.
>>>>>>> f96c0e0 (se agrega mi proyecto)


segunda version de mi proyecto sumativa2 

Estructura del Proyecto
Aplicación principal: CRUD de productos, categorías, marcas y características.
Templates: register.html, result.html, index.html.
Filtros: Filtrar productos por marca, categoría y características.

# Gestión de Productos S.A.

Proyecto de Django para la gestión de productos, permitiendo CRUD de productos con categorías, marcas y características.

## Requisitos
- Python 3.x
- Django 4.x
- Git

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd gestion_productos

  2. Realiza las migraciones de la base de datos:

  python manage.py migrate.

  3.Crea un superusuario:

  python manage.py createsuperuser

  4.Ejecuta el servidor de desarrollo:

  python manage.py runserver

  5.Accede a la aplicación en tu navegador:

  http://localhost:8000/admin/

  6.http://localhost:8000/productos


  # Proyecto API con JWT

Este proyecto implementa un sistema de autenticación basado en JSON Web Tokens (JWT) utilizando Django y Django REST Framework. A continuación, se describe cómo configurar y utilizar la API.

## Configuración Inicial

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno:
   - Crea un archivo `.env` en la raíz del proyecto.
   - Agrega la siguiente información al archivo `.env`:
     ```env
     SECRET_KEY=tu_secreto
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
     ```

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Crea un superusuario para acceder al panel de administración:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

## Uso de la API

### Endpoints Principales

1. **Obtener Token de Acceso y Refresco:**
   - URL: `/api/token/`
   - Método: POST
   - Cuerpo de la solicitud:
     ```json
     {
       "username": "usuario_prueba",
       "password": "contraseña_prueba"
     }
     ```
   - Respuesta:
     ```json
     {
       "access": "<token_de_acceso>",
       "refresh": "<token_de_refresco>"
     }
     ```

2. **Refrescar Token de Acceso:**
   - URL: `/api/token/refresh/`
   - Método: POST
   - Cuerpo de la solicitud:
     ```json
     {
       "refresh": "<token_de_refresco>"
     }
     ```
   - Respuesta:
     ```json
     {
       "access": "<nuevo_token_de_acceso>"
     }
     ```

3. **Endpoints Protegidos:**
   Para acceder a los endpoints protegidos, incluye el token de acceso en el encabezado de la solicitud:
   ```
   Authorization: Bearer <token_de_acceso>
   ```

### Usuario de Prueba

- **Usuario:** `usuario_prueba`
- **Contraseña:** `contraseña_prueba`

Este usuario ha sido creado para facilitar las pruebas iniciales.

## Documentación

La documentación completa de la API está disponible en la siguiente dirección:

```
http://localhost:8000/docs/
```

Esta documentación fue generada utilizando Swagger/OpenAPI y contiene detalles sobre todos los endpoints disponibles.

## Notas

- Asegúrate de que el servidor esté en ejecución antes de intentar acceder a los endpoints.
- Modifica las configuraciones según sea necesario para el entorno de producción (e.g., desactiva `DEBUG` y utiliza un secreto más seguro).
