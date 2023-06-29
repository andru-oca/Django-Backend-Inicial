## Django Parte II

Como arrancamos el proyecto:

```
vinoteca
├── manage.py
├── static
│   ├── css
│   │   └── main.css
│   ├── imgs
│   │   ├── fire.webp
│   │   ├── landing.webp
│   │   └── linux.png
│   └── js
│       ├── main.js
│       └── vueScript.js
├── templates
│   ├── base_vinoteca.html
│   └── index.html
└── vinoteca
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    └── wsgi.py
```

---

Los siguientes pasos son necesarios para poder seguir con el proyecto?

Generar un entorno virtual, en este caso usando las CodeSpaces que tiene una máquina virtual con la distribución de Ubuntu.

-   crear el virtualenv

```
$ virtualenv venv
```

-   activar el entorno virtual:

```
$ source venv/bin/activate
```

-   instalar las dependecias para usar Django

```
$ pip insall django
```

-   el proyecto deberá estar en el mismo nivel del venv

```
├──venv
├──vinoteca
    ├── manage.py
    ├── static
    ├── templates
    └── vinoteca
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── wsgi.py
```

-   ingresamos a la carpeta del proyecto

```
$ cd vinoteca
```

---

## PRIMERA PARTE

### Integracion con el backend de django

> En este contexto ya tenemos todo para generar la integración con una base de datos, en donde estaremos utilizando una modularización del proyecto con apps, que me permite gestionar las modificaciones, ediciones y visualización de los registros existentes en la base de datos que podemos registrar en el archivo de settings del proyecto.

-   Generar un app, en este caso estamos usando el nombre de app_vino, pues vamos a realizar un CRUD de estos productos.

```
$ python manage.py startapp app_vino
```

-   Generamos un Modelo:

[Documentación](https://docs.djangoproject.com/en/4.2/topics/db/models/)

-   Que es un modelo? Un modelo es una abstracción de una tabla de una base de datos, usando una ORM de Django, el cual nos permite trabajar directamente con metodos y atributos que son registrados en la clase creada. \
    Para el siguiente caso vamos a realizar un Modelo simple: _app_vino/models.py_

```
class Vino(models.Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    nombre  =  models.CharField(max_length=200)
    rating  = models.PositiveSmallIntegerField(blank=False,null=False)
    abv     = models.FloatField(blank=True, null=True)

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    # class Meta:
    #    db_table = "vinos_table"


    def __str__(self):
        return f"El vino: {self.nombre}, Rating {self.abv}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]

```

-   Posterior necesitamos registrarlo de manera local en la app, por lo tanto necesitamos registro en el archivo de _app_vino/admin.py_

```
@admin.register(Vino)
class VinosAdmin(admin.ModelAdmin):
    ...
```

-   Con esa parte registrada ya podemos hacer gestiones de los registros directamente en el backend de django? Casi, pues necesitamos registrarlo en los settings del proyecto.
    Como buena practica se recomienda especificar en que lugar van seteados las apps que son customizadas y no vienen por defecto en django, por lo cual se crea una lista APPS

```
APPS = [
    "app_vino"
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += APPS
```

En esta etapa ya tenemos el registro de la app, logrando hacer una integracion con el admin de django.
Para acceder al sector de admin de django, necesitamos crear un super usuario, sin embargo vamos a tener alguna dificultad para que suceda eso, porque? pues , necesitamos tener una base de datos, por defecto tenemos sqlite3 que es una base de datos de menor potencia, por lo que nos da la facilidad de estar probando constantemente y rompiendola si es necesario para que en produccion no tengamos esa dificultad.

Entonces para generarlo hay que crear la base de datos y hacer las migraciones respectivas.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Al generar estas migraciones podemos llegar a observar que el archivo sqlite3 tiene las tablas creadas por medio de esa migracion.

```
$ python manage.py createsuperuser
```

Con esos pasos y siguiendo requisitos para generar el usuario y logrando acceder al admin de django. La pregunta general es como hacemos para entrar?

Accedemos al path : http://127.0.0.1:8000/admin

Accedemos a esa ruta y podemos crear un registro del articulo que hemos generado con la abstraccion del ORM (object relational mapper) [Documentacion](https://docs.djangoproject.com/en/4.2/topics/db/queries/)

Con esa creacion del registro podemos ver en la tabla destinada a la app y la tabla de vino.

Si bien esta es una forma sencilla de manejar la base de datos con la creacion de los elementos en django, esta no es la forma idonea para el usuario final de generarlos.
Por ende vamos a trabajar con la parte del front-end, lo cual estaremos utilizando la creacion de templates internos de la app y al mismo tiempo vamos trabajar con las views genericas de django y las urls de django; otra parte muy importante de django es que al hacer algunas modificaciones en los templates para que las rutas gestionadas por jinja nos permita redireccionarlo a los paths creados en los routers de django.

---

## SEGUNDA PARTE

### Integracion con el front-end

En este sector nuestro proyecto tendra la siguiente estructura:

```
vinoteca
├── app_vino
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── vino_create.html
│   │   ├── vino_delete.html
│   │   ├── vino_detail.html
│   │   └── vinos.html
│   ├── urls.py
│   └── views.py
├── manage.py
├── static
│   ├── css
│   │   └── main.css
│   ├── imgs
│   │   ├── fire.webp
│   │   ├── landing.webp
│   │   └── linux.png
│   └── js
│       ├── main.js
│       └── vueScript.js
├── templates
│   ├── base_vinoteca.html
│   └── index.html
└── vinoteca
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    └── wsgi.py
```

En ella podremos observar que estaremos agregando una nueva carpeta que se llamara templates, pero dentro de la app, las cuales tendran elementos importantes para el creado, modificado y listado de los vinos creados por el usuario y gestionado desde el front end.

En estos casos necesitamos integrar las views , urls y templates, para que podamos gestionar un crud sencillo pero que sea de manera dinamica. Estas creaciones y modificaciones son necesarias para poder integrarlo con el front.

En primera instancia vamos a crear un archivo dentro de la app que se llamara urls.py, pues no viene creado por defecto pero si es necesario que lo tengamos creado para hacer uso de las rutas que genera esta app, nos paramos en la ruta de _app_vino_

```
$ touch urls.py
```

Al crear esa ruta, podemos pasar a crea las views, las cuales manejaran la siguientes logicas de creacion, modificacion, actualizcion, borrado y muestra de todos los registros, vinos y el detalle de cada vino.

_views.py_

```
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Vino

# Create your views here.


class VinosBaseView(View):
    template_name = 'vinos.html'
    model = Vino
    fields = '__all__'
    success_url = reverse_lazy('vinos:all')


class VinosListView(VinosBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """

class VinosDetailView(VinosBaseView,DetailView):
    template_name = "vino_detail.html"

class VinosCreateView(VinosBaseView,CreateView):
    template_name = "vino_create.html"
    extra_context = {
        "tipo": "Crear vino"
    }


class VinosUpdateView(VinosBaseView,UpdateView):
    template_name = "vino_create.html"
    extra_context = {
        "tipo": "Actualizar vino"
    }

class VinosDeleteView(VinosBaseView,DeleteView):
    template_name = "vino_delete.html"
    extra_context = {
        "tipo": "Borrar vino"
    }

```

En esta ocasion lo que vamos a realizar es crear una clase base VinosBaseView, la cual por medio de herencia para a poder pasar los atributos de clase para las siguientes views, sin necesidad de volver a escribir el codigo muchas veces.

En cada uno se le indica el tipo de template necesario para cada una de las rutas necesarias.

Siguiente tendremos que generar las rutas en el archivo _urls.py_, de tal forma que vamos a indicarle los lugares a donde estaria ingresando desde el front.

```
from django.contrib import admin
from django.urls import path , include


from .views import      VinosListView   \
                    ,   VinosDetailView \
                    ,   VinosCreateView \
                    ,   VinosUpdateView \
                    ,   VinosDeleteView

app_name = "vinos"

urlpatterns = [
    path("", VinosListView.as_view(), name="all"),
    path("create/", VinosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", VinosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", VinosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", VinosDeleteView.as_view(), name="delete")

]
```

**Estas rutas son importante entender el app_name y como funciona los name, pues son de vital importancia en las rutas en los templates**

-   Algo interesante de estas clases es que ya tiene integrado un elemento integrado de creacion de formularios, las cuales las estamos obviando por que le dejamos el trabajo realizado directamente a django.

Verifiquemos algunos de los archivos de la carpeta templates de la app, por ejemplo : _vino_create.html_

```
{% extends 'base_vinoteca.html' %}
{% block content %}

<main>
    <div class="main-color-vinos">
        <h1>CREAR VINO</h1>
        <form method="post">

            {% csrf_token %}
            <div>{{form.as_p}}</div>
            <input type="submit" value="{{ tipo }}" />

        </form>

        <a href="{% url 'vinos:all' %}">Volvamos al Inicio</a>
    </div>
</main>
{% endblock %}

```

-   **csrf_token** : me permite validar la informacion de fuentes cruzadas.
-   **form.as_p** : me genera automaticamente el formulario, sin necesidad de crear un archivo _forms.py_, pues es algo para customizar por medio de los modelos creados.

-   Como ultimo paso debo integrar a la ruta del proyecto como lo indicamos en el siguiente archivo:

```
from django.contrib import admin
from django.urls import path , include

from .views import Vinoteca

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Vinoteca.as_view(), name="vinoteca"),
    # para indicar la ruta de los vinos junto con los indicados en
    # el urlpatterns de la app
    path("vinos/", include("app_vino.urls")),
]

```

Con esto ya tenemos la integracion del back-end (bases de datos) y con el front-end, utilizando las views integradas con los generics de django

---

## TERCERA PARTE

### Creacion de una API rest utilizando django-rest-framework

-   En esta integracion, para generar una api con un modulo que se llama rest_framework, para la cual necesitamos instalar la siguiente dependecia [django_rest_framework](https://www.django-rest-framework.org/):

```
$ pip install djangorestframework

```

Al integrarlo vamos a trabajar en unos modulos que deberan tener el siguiente formato, pues son los que integra lo necesario del paquete.

**serializers.py** : esto realiza una transformacion de los registros en un formato del tipo json, que va a ser la respuesta de la api

```
from rest_framework.serializers import ModelSerializer
from .models import Vino

class VinoSerializer(ModelSerializer):
    class Meta:
        model = Vino
        fields = "__all__"
```

**viewsets.py** : estos me permite tener unas vistas direccionadas al modelo junto con el queryset determinado

```
from rest_framework.viewsets import ModelViewSet
from .models import Vino
from .serializers import VinoSerializer

class VinoViewSet(ModelViewSet):
    queryset = Vino.objects.all()
    serializer_class = VinoSerializer
```

**router.py** : Esto me genera las rutas que van a integrarse a los paths de los que vaya a indicarle, en este caso sera de la siguiente forma.

```
from rest_framework import routers
from .viewsets import VinoViewSet

router = routers.SimpleRouter()

# en este caso se le anexa a la ruta de las urls de la app
router.register("api-vino",VinoViewSet)

```

_urls.py_

```
from django.urls import path
from .router import router

from .views import      VinosListView   \
                    ,   VinosDetailView \
                    ,   VinosCreateView \
                    ,   VinosUpdateView \
                    ,   VinosDeleteView

app_name = "vinos"

urlpatterns = [
    path("", VinosListView.as_view(), name="all"),
    path("create/", VinosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", VinosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", VinosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", VinosDeleteView.as_view(), name="delete")

]

urlpatterns += router.urls
```

-   Como ultimo detalle es importante colocar la app de rest_framework en los settings.

**settings.py**

```
# Application definition


APPS = [
    "vino_app"
]

EXTERNALS = [
    "rest_framework"
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


INSTALLED_APPS += APPS
INSTALLED_APPS += EXTERNALS

```

Con eso ya podemos acceder a la ruta :

https://127.0.0.1:8000/vinos/api-vino/

## Resumen

Algo que viene incorporado con django es un ORM, que me permite crear una app, en donde puedo utilizar para hacer interacciones con las bases de datos.
Pensemos que sea el caso que necesitemos interactuar, guardar e incorporar.

Cuando eso es necesario en django es necesario generar una app.

Pasos para realizarlos:

-   django-admin startapp <nombre_de_app> : Genera varios archivos de las cuales principalmente me permite trabajar con una base de datos, en un principio va a ser con sqlite (detalle a tener en cuenta algo que genera algo llamado migrations)
-   crear un model (viene por herencia tambien usando de django los models.Model)
-   registrarlo en la parte de la admisitracion, si bien existen dos formas, en lo particular suelo recomendar realizar usando el decorador.

-   Generar unas views utilizando las clases genericas de django
    [INFORMACION EXTRA DE COMO CREAR UN CRUD](https://towardsdatascience.com/build-a-django-crud-app-by-using-class-based-views-12bc69d36ab6)

Generacion CRUD

-   MODELS ==> Podriamos usar mas conexiones entre varios de estas tablas y/o modelos, sin embargo a modo practico solamente lo vamos a tener en 1 solo modelo
-   URLS => Es importante ir colocando donde debemos ir colocano los puntos a donde van colocando cada uno de los recursos del CRUD

---

ESTA PARTE ES ADICIONAL, SIN EMBARGO CON ESTO GENERAMOS NUESTRA PRIMER API USANDO DJANGO-

-   INTEGRACION CON LOS SERIALIZERS Y LAS VIEWS REQUERIDAS
-   [RESTApi](https://blog.logrocket.com/django-rest-framework-create-api/#utm_source%3Dhashnode%26utm_medium%3Dhashnode%2Brix%26utm_campaign%3Drix_chatbot_answer)
-   CREACION DE UNA API
