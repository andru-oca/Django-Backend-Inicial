## Django Parte II

## Integración con una ORM

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
