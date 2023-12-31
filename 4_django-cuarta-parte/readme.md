# Documentacion de esta API
- Se genera entorno de una API usando DRF, pillow y simpleJWT

- Dependecias detalladas en el archivo de requirements.txt

```
    $ pip install -r requirements.txt
```


## API Routes Documentation

### Authentication

-   **Obtain Token**
    -   Method: POST
    -   URL: `/api/token/`
    -   Description: Generates an access token by providing valid credentials (username and password).
    -   Headers: None
    -   Body: `username`, `password`
-   **Refresh Token**

    -   Method: POST
    -   URL: `/api/token/refresh/`
    -   Description: Generates a new access token using a refresh token.
    -   Headers: None
    -   Body: `refresh`

-   **Verify Token**
    -   Method: POST
    -   URL: `/api/token/verify/`
    -   Description: Verifies the authenticity of an access token.
    -   Headers: None
    -   Body: `token`

### Product-related Endpoints

-   **List/Create Products**

    -   Method: GET, POST
    -   URL: `/api/products/`
    -   Description: Lists all products or creates a new product.
    -   Headers: `Authorization: Bearer <access_token>`
    -   Body (for POST): Product data

-   **Retrieve/Update/Delete Product**
    -   Method: GET, PUT, DELETE
    -   URL: `/api/products/<id>/`
    -   Description: Retrieves, updates, or deletes a specific product by ID.
    -   Headers: `Authorization: Bearer <access_token>`

### Image-related Endpoints

-   **List/Create Images**

    -   Method: GET, POST
    -   URL: `/api/images/`
    -   Description: Lists all images or uploads a new image.
    -   Headers: `Authorization: Bearer <access_token>`
    -   Body (for POST): Image data

-   **Retrieve/Update/Delete Image**
    -   Method: GET, PUT, DELETE
    -   URL: `/api/images/<id>/`
    -   Description: Retrieves, updates, or deletes a specific image by ID.
    -   Headers: `Authorization: Bearer <access_token>`

### Admin

-   **Admin Panel**
    -   Method: GET
    -   URL: `/admin/`
    -   Description: Access to Django admin panel for administration purposes.

### Static Media URLs

-   **Media URLs**
    -   URL: `/media/`
    -   Description: Access to uploaded media files.

## PARA GENERAR EL TOKEN

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://localhost:8000/api/token/
```

## PARA CONSUMIR CON EL TOKEN

```
curl \
  -H "Authorization: Bearer <token>" \
  http://localhost:8000/api/some-protected-view/
```

## PARA REFRESCAR EL TOKEN

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<token>"}' \
  http://localhost:8000/api/token/refresh/
```
