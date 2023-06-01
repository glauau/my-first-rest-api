# read.me

# my-first-rest-api

Este projeto tem como objetivo construir uma Rest API utilizando o framework Flask.
Para exemplificar, sera construído um sistema onde é possível criar lojas e itens através de requisicoes HTTP feitas utilizando o software Insomnia.

**Obs:**
Para iniciar, primeiro é necessario fazer o build da imagem e depois executar o container:
`docker build -t my-first-api .`

`docker run -p 5000:5000 $image_id`

**Obs2:**
Requests para serem executadas no Insomnia:

- Criar uma loja:

```bash
curl --request POST \
  --url http://localhost:5000/store \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "My store 2"
}'
```

- Retornar infos sobre uma loja:

```bash
curl --request GET \
  --url http://localhost:5000/store/My%20Store
```

- Retornando itens de uma loja especifica:

```bash
curl --request GET \
  --url http://localhost:5000/store/mystores/item
```
