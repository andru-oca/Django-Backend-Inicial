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
[PRINCIPIO DE SoC](https://dev.to/tamerlang/separation-of-concerns-the-simple-way-4jp2)

-   IMPLEMENTAR UN PROYECTO ARMADO EN FRONTEND y enlazado.

SAMPLE : https://github.com/andru-oca/clase_21.git


Practica Vinoteca
---

```
virtualenv venv

```

activacion del entorno virtual


```
source venv/bin/activate

```

El proyecto integracion lo podemos integrar colocando las dependencias de un archivo de texto.
_requirements.txt_

```
$ pip install -r requirements.txt

```
Con esto ya podemos integrar nuestro front.
Creamos nuestro proyecto con django:

```
$ django-admin startproject vinoteca .
```

Creamos una vista que me va a permitir realizar un endpoint para la ruta de nuestra pagina, en esta ocasion se realiza para el inicio con el elemento index el cual esta usando un template de jinja.


Es necesario entender la primera logica que teniamos con las vistas, las cuales por medio de una ruta, va a devolver informacion, en este caso un return de la respuesta de un request del tipo GET al servidor de django:

```
from django.views.generic import TemplateView

class Vinoteca(TemplateView):
    template_name = "index.html"
    
```

Esa TemplateView son implementaciones genericas ya determinadas por django.

Posterior tenemos que indicarle las rutas en el archivo _urls.py_ del proyecto:

```
from django.contrib import admin
from django.urls import path , include

from .views import Vinoteca

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Vinoteca.as_view(), name="vinoteca")
]

    
```

En este caso importamos la clase Vinoteca y usamos uno de los metodos heredados de la clase TemplateView , el cual es as_view(), le indicamos el name el cual sera el alias que va a reconocer internamente el framework

Antes del final es necesario entender los templates, esa carpeta de template es muy importante de de colocar los archivos html que utilizamos para el proyecto, el mismo va a tener sintaxis jinja que me va a permitir renderizar sectores de codigos de manera mas sencilla.
Sin embargo esto hay que tamabien declararlo en los settings del proyecto:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```


Con esto le declaramos que a partir de la ruta raiz tendremos la carpeta templates: **vinoteca**/templates


Por ultimo hay que configurar los _settigns.py_ para poder tener los staticos de esa pagina 

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"
```
Con esto ya colocado ya tendremos el proyecto de front end integrado al servidor que trae el framework de django

