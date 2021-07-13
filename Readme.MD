Instalando o projeto:

Baixe o projeto e extraia em uma pasta

(Opcional) Inicie um ambiente virtual com virtualenv

Execute: 
```
pip install -r requirements.txt
```

Execute o servidor: 
```
python manage.py runserver
```

Utilize a API usando os métodos listados abaixo

Classe Usuário:
```
GET /usuarios/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept


[
    {
        "id": ,
        "name": "",
        "cpf": ""
    }
]


GET /usuarios/<id>/

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": ,
    "name": "",
    "cpf": ""
}
```

Classe Categorias:

```
GET /categorias/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": ,
        "name": ""
    }
]

GET /categorias/<id>/

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": ,
    "name": ""
}
```

Classe	Produtos:

```
GET /produtos/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": ,
        "name": "",
        "price": 0.0,
        "category": <id-categorias>
    }
]

GET /produtos/<id>/

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"id": ,
	"name": "",
	"price": 0.0,
	"category": <id-categorias>
}
```

Classe Pedidos

```
GET /pedidos/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": ,
        "total": 0.0,
        "invoice_date": "YYYY-MM-DD",
        "user": <id-usuarios>,
        "products": [
            <id-produtos>,
			<id-produtos>
        ]
    }
]

GET /pedidos/<id>/

{
	"id": ,
	"total": 0.0,
	"invoice_date": "YYYY-MM-DD",
	"user": <id-usuarios>,
	"products": [
		<id-produtos>,
		<id-produtos>
	]
}
```