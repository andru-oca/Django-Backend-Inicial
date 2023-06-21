## Django Parte I

Django es un FrameWork web de código abierto escrito en Python que permite el desarrollo rápido y sencillo de sitios web seguros y mantenibles. Algunos puntos importantes sobre Django son:

-   Django sigue la filosofía "Baterías incluidas" donde provee casi todas las características que los desarrolladores necesitan para crear sitios web.
-   Django puede usarse para crear casi cualquier tipo de sitio web como sistemas de CMS, sitios de noticias, redes sociales, etc.
-   Django ayuda a evitar errores comunes de seguridad al proveer protecciones integradas y siguiendo prácticas seguras por defecto.
-   Django es escalable gracias a su arquitectura desacoplada que permite agregar hardware adicional para aumentar el tráfico.
-   El código de Django está escrito usando principios de diseño que fomentan la creación de código mantenible y reutilizable.

Para crear una aplicación en Django se siguen estos pasos:

1. Se crea el proyecto Django usando el comando django-admin startproject nombre_proyecto
2. Dentro del proyecto se crean las aplicaciones usando el comando python manage.py startapp nombre_app
3. Se registran los modelos de la aplicación en el archivo models.py
4. Se crean las migraciones con el comando python manage.py makemigrations
5. Se aplican las migraciones con el comando python manage.py migrate
6. Se crean las vistas en el archivo views.py y se mapean a URLs en urls.py
7. Se definen las plantillas HTML en la carpeta templates

---

Temas a tratar : [Django](https://www.djangoproject.com/) en general.

-   Modelo que usa Django
    -   [MVT](https://www.geeksforgeeks.org/django-project-mvt-structure/)
    -   [MVT DJANGO](https://www.youtube.com/watch?v=cyP4Uw2b2XM)
-   MVT vs MVT Diferencias: [PATRONES DE DISEÑO](https://www.youtube.com/watch?v=zhSDjntidws)
-   Que tiene incluído?
    -   ORM
    -   Jinja Templates Modelado
    -   Dev's tiene la posibilidad de generar un server de una sola
    -   URL's Pattern Sencillo

> Importante:
> En Django existen dos formas de trabajar: CBV(con codigo reutilizable) y/o Functions Base View , que está pensado para codigos sencillos y simples, pero tiene una gran problematica, no escala para proyectos con mayor complejidad.

---

Procesos:

-   Instalación de Framework Django
-   Levantar primer Django HomePage
-   Entender las primeras etapas de Settings
-   Entender Views
-   Entender las URLS

Pasos:

-   Generar un virtualenv :

    -   en linux virtualenv venv | en windows python -m venv <nombre_proyecto:generalmente VENV>

    -   instalar django :
        ```
        pip install django
        ```
    -   crear un proyecto con el comando:

        ```
        django-admin startproject <nombre_proyecto>
        ```

    -   run server:
        ```
        python manage.py runserver <PORT a eleccion>(por default es 8000)
        ```
    -   crear una vista simple con FunctionBase View vs Django ClassBase View

[Bibliografia extra](https://docs.hektorprofe.net/django/web-personal/patron-mvt-modelo-vista-template/)

-   IMPLEMENTAR UN PROYECTO ARMADO EN FRONTEND y enlazado.

SAMPLE : https://github.com/andru-oca/clase_21.git
