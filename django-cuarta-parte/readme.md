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
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/api/some-protected-view/
```

## PARA REFRESCAR EL TOKEN

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/token/refresh/
```
