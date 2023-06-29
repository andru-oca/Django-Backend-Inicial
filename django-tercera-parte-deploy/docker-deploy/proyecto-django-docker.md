Deploy Contenedores
---

El archivo docker-compose.yml presenta 3 servicios principales

-   mysql(base de datos)
-   nginx(web server)
-   django(entorno integrado de backend y front)


---

Generar un las variables de entorno para correr el proyecto en la carpeta .env_variables/produccion.env, ejemplo :
_produccion.env_

```

DJANGO_SECRET_KEY = <clave_encryptada>
DJANGO_ALLOWED_HOSTS = localhost,127.0.0.1,0.0.0.0,[::1],django,*

```
---

Puesta en produccion:

```
sudo docker compose up -d --build

```

