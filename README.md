# read.me

# my-first-rest-api

Este projeto tem como objetivo construir uma Rest API utilizando o framework Flask.
Para exemplificar, sera construído um sistema onde será possível criar lojas e itens dentro das mesmas através de requisicoes feitas utilizando o software Insomnia.

**Obs:**
Para iniciar, primeiro será necessario fazer o build da imagem em que a aplicacao ja sera executada:
`docker build -t my-first-api .`

`docker run -p 5000:5000`

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
