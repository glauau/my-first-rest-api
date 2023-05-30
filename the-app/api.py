import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)

stores = [
    {
    "name": "My Store",
    "items":[
        {
            "name": "Chair",
            "price": "15.99"
        }
    ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex #vai gerar um id
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores: #varre a lista de lojas
        if store ["name"] == name: #verifica se o nome da loja combina com o nome passado na url
            new_item = {"name": request_data["name"], "price": request_data["price"]} #montando um dicionario com duas chaves
            store["items"].append(new_item)
            return new_item, 201
    return {"message:" "store not found"}, 404 #caso tente criar itens em uma loja inexistente

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message:" "store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message:" "store not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")

